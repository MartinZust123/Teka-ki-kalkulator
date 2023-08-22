import os

from bottleext import get, post, run, request, template, redirect, static_file, url, response#, template_user
import bottle # naprej uporabljamo bottleext

from data.Database import Repo
from data.Modeli import *
from data.Services import AuthService
from functools import wraps

SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

repo = Repo()
auth = AuthService(repo)

import bottle
import naiven_tekaski_kalkulator
import running_calculator as rc
from fetch_table_data import fetch_table_data

#=================================================================================================#

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

#=================================================================================================#

@bottle.get("/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

@bottle.get("/odjava/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

#=================================================================================================#

@bottle.get("/prijava/")
def vrni_prijavo():
    return bottle.template("prijava.html")

@bottle.post("/prijavi_se/")
def prijava():
    username = bottle.request.query["username"]
    geslo = bottle.request.query["password"]

    if not auth.obstaja_uporabnik(username):
        return template("views/registracija.html", napaka="Uporabnik s tem imenom ne obstaja")

    prijava = auth.prijavi_uporabnika(username, geslo)

    if prijava:
        bottle.response.set_cookie("uporabnisko_ime", username)
        return redirect(url('zacetna_stran'))
    else:
        return template("prijava.html", napaka="Neuspešna prijava. Napačno geslo ali uporabniško ime.")
    

@bottle.get("/registracija/")
def registracija():
    return bottle.template("registracija.html")

@bottle.post("/registriraj_se/")
def registriraj_se():
    """ Če je registracija uspešna, uporabnika prijavi in ustvari piškotke. """

    geslo = bottle.request.query["password"]
    geslo1 = bottle.request.query["password1"]
    username1 = bottle.request.query["username1"]
    ime = bottle.request.query["name"]
    starost = bottle.request.query["age"]
    spol = bottle.request.query["gender"]

    if geslo != geslo1:
        return bottle.template("registracija1.html")
    else:
        if auth.dodaj_uporabnika(username1, ime, geslo, spol, starost):
            prijava = auth.prijavi_uporabnika(username1, geslo)
        else:
            return bottle.template("registracija1.html", napaka="Uporabnik s tem že obstaja")
        
        if prijava:
            response.set_cookie("uporabnisko_ime", username1, "secret")
            return redirect(url('zacetna_stran')) #na katero stran naj vrze po prijavi???
        
#=================================================================================================#

@bottle.get("/uredi_profil/")
#@cookie_required
def uredi_profil():
    ime = bottle.request.query["ime"]
    priimek = bottle.request.query["priimek"]
    starost = bottle.request.query["starost"]
    return bottle.template("uredi_profil.html",ime=ime, priimek=priimek,starost=starost)

@bottle.get("/posodobi_profil/")
#@cookie_required
def posodobi_profil():
    geslo = bottle.request.query["password"]
    geslo1 = bottle.request.query["password1"]
    username1 = bottle.request.query["username1"]
    ime = bottle.request.query["name"]
    starost = bottle.request.query["age"]
    if geslo != geslo1:
        return bottle.template("registracija1.html")
    else:
        return bottle.template("zacentna_stran.html", username= username1)

@bottle.get("/rezultati/")
#@cookie_required
def rezultati_tekov():
    return bottle.template("rezultati.html")

@bottle.get("/prikazi_rezultate/")
def prikazi_rezultate():
    maraton = bottle.request.query["maraton"]
    if maraton == "mali_kraski_maraton":
        maraton = "kraski"
    razdalja = bottle.request.query["razdalja"]
    letnica = bottle.request.query["letnica"]
    spol = bottle.request.query["spol"]
    if spol == "moški":
        spol = "M"
    else:
        spol = "Z"
    tabela = fetch_table_data(int(letnica), maraton, int(razdalja), spol)
    return bottle.template("rezultati1.html", tabela=tabela)


@bottle.get("/kalkulator/")
def vrni_kalkulator():
    return bottle.template("kalkulator.html")

@bottle.get("/statistika/")
def vrni_statistiko():
    return bottle.template("statistika.html", ime="Ioann", priimek="Stanković", starost="26", spol="moški")

@bottle.get("/kraski22_10m/")
def kraski22_10():
    return bottle.template("2022_kraski_10_Mn.html")

@bottle.get("/blejski22_10m/")
def blejski22_m():
    return bottle.template("2022_blejski_Mn.html")

@bottle.get("/ljub22_10m/")
def ljubljanski22_m():
    return bottle.template("2022_ljubljanski_10_M.html")

@bottle.get("/kranj22_10m/")
def kranjski22_10m():
    return bottle.template("2022_kranjski_10_Mn.html")

@bottle.get("/kraski22_10z/")
def kraski22_10z():
    return bottle.template("2022_kraski_10_Z.html")

@bottle.get("/blejski22_10z/")
def blejski22_m():
    return bottle.template("2019_nocna_10_Z.html")

@bottle.get("/ljub22_10z/")
def ljubljanski22_m():
    return bottle.template("2021_ljubljanski_10_Z.html")

@bottle.get("/kranj22_10z/")
def kranjski22_10m():
    return bottle.template("2022_kranj_10_Z.html")

@bottle.get("/preracunaj/")
def preracunaj_get():
    pretecena = bottle.request.query["pretecena"]
    minute = bottle.request.query["min"]
    sek = bottle.request.query["sek"]
    zeljena = bottle.request.query["zeljena"]
    starost = bottle.request.query["starost"]
    cas = rc.running_calc(int(pretecena)*1000, int(minute)*60 + int(sek), int(zeljena)*1000, int(starost))
    #nove_min = int(cas // 1)
    #nove_sek = int(((cas - nove_min) * 60) // 1)
    return bottle.template("kalkulator1.html", pretecena = pretecena, minute = minute, sek = sek, zeljena = zeljena, starost = starost, cas=cas)



@bottle.get("/static/<filepath:path>")
def vrni_staticno_datoteko(filepath):
    return bottle.static_file(filepath, 'static')

bottle.run(reloader=True)