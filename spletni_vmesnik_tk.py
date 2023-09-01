import os

from bottleext import get, post, run, request, template, redirect, static_file, url, response #, template_user
import bottle 

from data.Database import Repo
from data.Modeli import *
from data.Services import AuthService
from functools import wraps

SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

repo = Repo()
auth = AuthService(repo)

import naiven_tekaski_kalkulator
import running_calculator as rc
from fetch_table_data import fetch_table_data

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
    return bottle.template("zacetna_stran_tk.html")


@get("/prva/")
@cookie_required
def prva():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    return bottle.template("zacetna_stran.html", username=uporabnik)

@get("/odjava/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

#= PRIJAVA, ODJAVA, REGISTRACIJA =================================================================#

@get("/prijava/")
def vrni_prijavo():
    return bottle.template("prijava.html")

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
    return bottle.template("registracija.html")

@post("/registracija/")
def registriraj_se():
    geslo = bottle.request.forms.getunicode("password")
    geslo1 = bottle.request.forms.getunicode("password1")
    username = bottle.request.forms.getunicode("username")
    ime = bottle.request.forms.getunicode("name")
    starost = bottle.request.forms.getunicode("age")
    spol = bottle.request.forms.getunicode("gender")

    
    if geslo != geslo1:
        return bottle.template("registracija.html", napaka="Gesli se ne ujemata")
    else:
        print(Uporabnik("", username, ime, geslo, spol, starost))
        if auth.dodaj_uporabnika(username, ime, geslo, spol, starost):
            prijava = auth.prijavi_uporabnika(username, geslo)
        else:
            return bottle.template("registracija.html", napaka="Uporabnik s tem uporabniškim imenom že obstaja")
        
        if prijava:
            response.set_cookie("uporabnisko_ime", username, path="/")
            redirect("/prva/")

        
#= UREJANJE PROFILA ==============================================================================#

@get("/uredi_profil/")
#@cookie_required
def uredi_profil():
    ime = bottle.request.forms.getunicode("ime")
    priimek = bottle.request.forms.getunicode("priimek")
    starost = bottle.request.forms.getunicode("starost")
    return bottle.template("uredi_profil.html",ime=ime, priimek=priimek,starost=starost)

@get("/posodobi_profil/")
#@cookie_required
def posodobi_profil():
    geslo = bottle.request.forms.getunicode("password")
    geslo1 = bottle.request.forms.getunicode("password1")
    username1 = bottle.request.forms.getunicode("username1")
    ime = bottle.request.forms.getunicode("name")
    starost = bottle.request.forms.getunicode("age")
    if geslo != geslo1:
        return bottle.template("registracija1.html")
    else:
        return bottle.template("zacetna_stran.html", username= username1)
    
#= REZULTATI PRETEKLIH TEKMOVANJ =================================================================#

@get("/rezultati/")
def rezultati_tekov():
    return bottle.template("rezultati.html")

@get("/prikazi_rezultate/")
def prikazi_rezultate():
    maraton = bottle.request.forms.getunicode("maraton")
    if maraton == "mali_kraski_maraton":
        maraton = "kraski"
    elif maraton == "ljubljanski_maraton":
        maraton = "ljubljanski"
    elif maraton == "blejska_desetka":
        maraton = "bled"
    else:
        maraton = "kranj"
    # nocni manjka

    razdalja = bottle.request.forms.getunicode("razdalja")
    letnica = bottle.request.forms.getunicode("letnica")
    spol = bottle.request.forms.getunicode("spol")

    if spol == "moški":
        spol = "M"
    else:
        spol = "Z"

    tabela = repo.dobi_maraton(Rezultat, letnica, maraton, razdalja, spol)

#    tabela = fetch_table_data(int(letnica), maraton, int(razdalja), spol)
    return bottle.template("rezultati1.html", tabela=tabela)

#= TVOJA STATISTIKA ==============================================================================#

@get("/statistika/")
#@cookie_required
def vrni_statistiko():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")
    print(uporabnik) ###pobrisi
    u = repo.dobi_gen_id(Uporabnik, uporabnik, "username")
    return bottle.template("statistika.html", ime=u.imeinpriimek, starost=u.starost, spol=u.spol)
#    return bottle.template("statistika.html", ime="Ioann Stanković", starost="26", spol="moški")

@get("/tvoji_treningi/")
#@cookie_required
def prikazi_treninge():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")

    teki = repo.dobi_vse_gen_id(Tek, uporabnik, "tekac")

    return bottle.template("tvoji_treningi.html", tabela=teki)

@post("/tvoji_treningi/")
def vnesi_trening():
    uporabnik = bottle.request.get_cookie("uporabnisko_ime")

    datum = bottle.request.forms.getunicode("datum")
    razdalja = bottle.request.forms.getunicode("razdalja")
    cas = bottle.request.forms.getunicode("cas")

    trening = Tek(
        tekac=uporabnik,
        datum=datum,
        razdalja=razdalja,
        cas=cas
    )

    repo.dodaj_gen(trening) #naj bi manjkal nek permission zato noce commitat na bazo



#= TEKAŠKI KALKULATOR ============================================================================#

@get("/kalkulator/")
def vrni_kalkulator():
    return bottle.template("kalkulator.html")

@get("/preracunaj/")
def preracunaj_get():
    pretecena = bottle.request.forms.getunicode("pretecena")
    minute = bottle.request.forms.getunicode("min")
    sek = bottle.request.forms.getunicode("sek")
    zeljena = bottle.request.forms.getunicode("zeljena")
    starost = bottle.request.forms.getunicode("starost")
    cas = rc.running_calc(int(pretecena)*1000, int(minute)*60 + int(sek), int(zeljena)*1000, int(starost))
    #nove_min = int(cas // 1)
    #nove_sek = int(((cas - nove_min) * 60) // 1)
    return bottle.template("kalkulator1.html", pretecena = pretecena, minute = minute, sek = sek, zeljena = zeljena, starost = starost, cas=cas)

bottle.run(reloader=True)