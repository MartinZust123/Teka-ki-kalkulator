import os

from bottleext import get, post, run, request, template, redirect, static_file, url, response#, template_user
import bottle 

##
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
    return bottle.static_file(filepath, 'static')

#= PIŠKOTKI ======================================================================================#

def cookie_required(f):
    """
    Dekorator, ki zahteva veljaven piškotek. Če piškotka ni, uporabnika preusmeri na stran za prijavo.
    """
    @wraps(f)
    def decorated( *args, **kwargs):
        cookie = request.get_cookie("uporabnik")
        if cookie:
            return f(*args, **kwargs)
        return template("prijava.html", uporabnik=None, napaka="Potrebna je prijava!")

    return decorated

#= PRVA STRAN ====================================================================================#

@get("/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

@get("/odjava/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

#= PRIJAVA =======================================================================================#

@get("/prijava/")
def vrni_prijavo():
    return bottle.template("prijava.html")

@post("/prijava/")
def prijava():
    username = bottle.request.forms.getunicode("username")
    geslo = bottle.request.forms.getunicode("password")

    if not auth.obstaja_uporabnik(username):
        return template("views/registracija.html", napaka="Uporabnik s tem imenom ne obstaja")

    prijava = auth.prijavi_uporabnika(username, geslo)

    if prijava:
        bottle.response.set_cookie("uporabnisko_ime", username)
        return template("zacetna_stran.html", username=username)
    else:
        return template("prijava.html", napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")
    

@get("/registracija/")
def registracija():
    return bottle.template("registracija.html")

@post("/registracija/")
def registriraj_se():
    """ Če je registracija uspešna, uporabnika prijavi in ustvari piškotke. """

    geslo = bottle.request.forms.getunicode("password")

    geslo1 = bottle.request.forms.getunicode("password1")
    username1 = bottle.request.forms.getunicode("username")
    ime = bottle.request.forms.getunicode("name")
    starost = bottle.request.forms.getunicode("age")
    spol = bottle.request.forms.getunicode("gender")

    if geslo != geslo1:
        return bottle.template("registracija1.html")
    else:
        if auth.dodaj_uporabnika(username1, ime, geslo, spol, starost):
            prijava = auth.prijavi_uporabnika(username1, geslo)
        else:
            return bottle.template("registracija1.html", napaka="Uporabnik s tem že obstaja")
        
        if prijava:
            response.set_cookie("uporabnisko_ime", username1, "secret")
            return template("zacetna_stran.html", username=username1)

        
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
    razdalja = bottle.request.forms.getunicode("razdalja")
    letnica = bottle.request.forms.getunicode("letnica")
    spol = bottle.request.forms.getunicode("spol")
    if spol == "moški":
        spol = "M"
    else:
        spol = "Z"
    tabela = fetch_table_data(int(letnica), maraton, int(razdalja), spol)
    return bottle.template("rezultati1.html", tabela=tabela)

#= TVOJA STATISTIKA ==============================================================================#

@get("/tvoji_treningi/")
#@cookie_required
def prikazi_treninge():

    uporabnik = bottle.request.get_cookie("uporabnik")
    teki = Repo.dobi_vse_gen_id(Tek, uporabnik, "uporabnik")

    return bottle.template("rezultati1.html", tabela=teki)

#    ime = bottle.request.forms.getunicode("ime")
#
#    tabela = moji_treningi(ime)
#    return bottle.template("rezultati1.html", tabela=tabela)

@get("/statistika/")
def vrni_statistiko():
    uporabnik = bottle.request.get_cookie("uporabnik")
    ime = uporabnik.imeinpriimek
    starost = ""
    spol = ""
    return bottle.template("statistika.html", ime="Ioann Stanković", starost="26", spol="moški")

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


@get("/kraski22_10m/")
def kraski22_10():
    return bottle.template("2022_kraski_10_Mn.html")

@get("/blejski22_10m/")
def blejski22_m():
    return bottle.template("2022_blejski_Mn.html")

@get("/ljub22_10m/")
def ljubljanski22_m():
    return bottle.template("2022_ljubljanski_10_M.html")

@get("/kranj22_10m/")
def kranjski22_10m():
    return bottle.template("2022_kranjski_10_Mn.html")

@get("/kraski22_10z/")
def kraski22_10z():
    return bottle.template("2022_kraski_10_Z.html")

@get("/blejski22_10z/")
def blejski22_m():
    return bottle.template("2019_nocna_10_Z.html")

@get("/ljub22_10z/")
def ljubljanski22_m():
    return bottle.template("2021_ljubljanski_10_Z.html")

@get("/kranj22_10z/")
def kranjski22_10m():
    return bottle.template("2022_kranj_10_Z.html")

bottle.run(reloader=True)