import os

from bottleext import get, post, template, redirect, static_file, response, url
import bottle 
import bcrypt

from data.Database import Repo
from data.Modeli import *
from data.Services import AuthService
from functools import wraps

SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

repo = Repo()
auth = AuthService(repo)

import running_calculator as rc
import vizualni_vmesnik as vv 

#= STATIČNE DATOTEKE =============================================================================#

@bottle.get("/static/<filepath:path>")
def vrni_staticno_datoteko(filepath):
    return static_file(filepath, 'static')

#= PIŠKOTKI ======================================================================================#

def cookie_required(f):
    """
    Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    """
    @wraps(f)
    def decorated( *args, **kwargs):
        cookie = bottle.request.get_cookie("uporabnisko_ime")
        if cookie:
            return f(*args, **kwargs)
        return template("prijava.html", uporabnik=None, napaka="Potrebna je prijava!")

    return decorated

#= PRVA STRAN ====================================================================================#

@get("/")
def prvi_zaslon():
    return template("zacetna_stran_tk.html")


@get("/prva/")
@cookie_required
def prva():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    return template("zacetna_stran.html", username=uporabnik)

@get("/odjava/")
def prvi_zaslon():
    return template("zacetna_stran_tk.html")

#= PRIJAVA, ODJAVA, REGISTRACIJA =================================================================#

@get("/prijava/")
def vrni_prijavo():
    return template("prijava.html")

@post("/prijava/")
def prijava():
    username = bottle.request.forms.getunicode("username")
    geslo = bottle.request.forms.getunicode("password")

    if not auth.obstaja_uporabnik(username):
        return template("registracija.html", napaka="Uporabnik s tem imenom ne obstaja")

    prijava = auth.prijavi_uporabnika(username, geslo)

    if prijava:
        response.set_cookie("uporabnisko_ime", username, path="/")
        redirect("/prva/")

    else:
        return template("prijava.html", napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")

@get("/odjava/")
def odjava():
    response.delete_cookie("uporabnisko_ime", path="/")
    redirect("/")

@get("/registracija/")
def registracija():
    return template("registracija.html", napaka=None)

@post("/registracija/")
def registriraj_se():
    geslo = bottle.request.forms.getunicode("password")
    geslo1 = bottle.request.forms.getunicode("password1")
    username = bottle.request.forms.getunicode("username")
    ime = bottle.request.forms.getunicode("name")
    starost = bottle.request.forms.getunicode("age")
    spol = bottle.request.forms.getunicode("gender")

    
    if geslo != geslo1:
        return template("registracija.html", napaka="Gesli se ne ujemata")
    else:
        if auth.dodaj_uporabnika(username, ime, geslo, spol, starost):
            prijava = auth.prijavi_uporabnika(username, geslo)
        else:
            return template("registracija.html", napaka="Uporabnik s tem uporabniškim imenom že obstaja")
        
        if prijava:
            response.set_cookie("uporabnisko_ime", username, path="/")
            redirect("/prva/")

        
#= UREJANJE PROFILA ==============================================================================#

@get("/uredi_profil/")
@cookie_required
def uredi_profil():
    return template("uredi_profil.html")

@post("/posodobi_profil/")
@cookie_required
def posodobi_profil():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    u = repo.dobi_gen_id(Uporabnik, uporabnik, "username")
    geslo = bottle.request.forms.getunicode("password")
    geslo1 = bottle.request.forms.getunicode("password1")
    ime = bottle.request.forms.getunicode("name")
    starost = bottle.request.forms.getunicode("year")

    if geslo != geslo1:
        return template("uredi_profil.html", napaka="Gesli se ne ujemata. Poskusi znova.")
    else:
        # kodiranje gesla
        bytes = geslo.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(bytes, salt)

        user = Uporabnik(
            id=u.id,
            username=uporabnik, 
            imeinpriimek=ime, 
            geslo=password_hash.decode(),
            spol=u.spol, 
            starost=starost
        )

        repo.posodobi_gen(user, "username")
        return template("zacetna_stran.html", username=uporabnik)
    
#= REZULTATI PRETEKLIH TEKMOVANJ =================================================================#

@get("/rezultati/")
def rezultati_tekov():
    return template("rezultati.html")

@post("/prikazi_rezultate/")
def prikazi_rezultate():
    maraton = bottle.request.forms.getunicode("maraton")
    if maraton == "mali_kraski_maraton":
        maraton = "kraski"
        izpis = "Mali Kraški maraton"
    elif maraton == "ljubljanski_maraton":
        maraton = "ljubljanski"
        izpis = "Ljubljanski maraton"
    elif maraton == "blejska_desetka":
        maraton = "bled"
        izpis = "Blejska desetka"
    else:
        maraton = "kranj"
        izpis = "Kranjski maraton"
    # nocni manjka

    razdalja = bottle.request.forms.getunicode("dist")
    letnica = bottle.request.forms.getunicode("year")
    spol = bottle.request.forms.getunicode("spol")

    if spol == "moški":
        spol = "M"
        sp = "moške"
    else:
        spol = "Z"
        sp = "ženske"
    
    order = bottle.request.forms.getunicode("order")
    if order == "pr_a":
        tabela = repo.dobi_maraton_ordered(Rezultat, letnica, maraton, razdalja, spol, "priimekinime")
    elif order == "pr_z":
        tabela = repo.dobi_maraton_ordered(Rezultat, letnica, maraton, razdalja, spol, "priimekinime", False)
    elif order == "age_old":
        tabela = repo.dobi_maraton_ordered(Rezultat, letnica, maraton, razdalja, spol, "lr")
    elif order == "age_young":
        tabela = repo.dobi_maraton_ordered(Rezultat, letnica, maraton, razdalja, spol, "lr", False)
    else:
        tabela = repo.dobi_maraton(Rezultat, letnica, maraton, razdalja, spol)

    return template("rezultati1.html", tabela=tabela, razdalja=razdalja, leto=letnica, kraj=izpis, sp=sp)

#= TVOJA STATISTIKA ==============================================================================#

@get("/statistika/")
@cookie_required
def vrni_statistiko():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    u = repo.dobi_gen_id(Uporabnik, uporabnik, "username")
    return template("statistika.html", ime=u.imeinpriimek, starost=u.starost, spol=u.spol)


@get("/tvoji_treningi/")
@cookie_required
def prikazi_treninge():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")

    teki = repo.dobi_vse_gen_id_ordered(Tek, uporabnik, "datum", False, "tekac")

    return template("tvoji_treningi.html", tabela=teki, username=uporabnik)

@post("/tvoji_treningi/")
@cookie_required
def vnesi_trening():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")

    datum = bottle.request.forms.getunicode("datum")
    razdalja = bottle.request.forms.getunicode("razdalja")
    min = int(bottle.request.forms.getunicode("cas_min"))
    sek = int(bottle.request.forms.getunicode("cas_sek"))
    cas = min*60 + sek

    trening = Tek(
        tekac=uporabnik,
        datum=datum,
        razdalja=razdalja,
        cas=cas
    )


    repo.dodaj_gen(trening) 
    redirect("/tvoji_treningi/")

@get("/vizualni_podatki/")
@cookie_required
def prikazi_vizualne_podatke():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    u = repo.dobi_gen_id(Uporabnik, uporabnik, "username")
    return template("vizualni_podatki.html", ime=u.imeinpriimek, starost=u.starost, spol=u.spol)

@get("/histogram_tempov/")
@cookie_required
def prikazi_histogram():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    teki = repo.dobi_vse_gen_id(Tek, uporabnik, "tekac")
    hist = vv.narisi_histogram_tempov(teki)
    return template("histogram.html", hist=hist)

@get("/izbrisi_tek/<id:int>/")
@cookie_required
def izbrisi_tek(id):    

    repo.izbrisi_gen(Tek, id)

    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    teki = repo.dobi_vse_gen_id_ordered(Tek, uporabnik, "datum", False, "tekac")
    return template("tvoji_treningi.html", tabela=teki, username=uporabnik)
   
#= TEKAŠKI KALKULATOR ============================================================================#

@get("/kalkulator/")
def vrni_kalkulator():
    return template("kalkulator.html")

@post("/preracunaj/")
def preracunaj_get():
    pretecena = bottle.request.forms.getunicode("pretecena")
    minute = bottle.request.forms.getunicode("min")
    sek = bottle.request.forms.getunicode("sek")
    zeljena = bottle.request.forms.getunicode("zeljena")
    starost = bottle.request.forms.getunicode("starost")
    utezi = rc.utezi 
    closest_utezi = rc.find_closest_value(int(zeljena), utezi)

    cas = rc.running_calc(int(pretecena)*1000, int(minute)*60 + int(sek), int(zeljena)*1000, int(starost), closest_utezi)
    return template("kalkulator1.html", pretecena = pretecena, minute = minute, sek = sek, zeljena = zeljena, starost = starost, cas=cas)

bottle.run(reloader=True)