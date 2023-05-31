import os

from bottleext import get, post, run, request, template, redirect, static_file, url, response, template_user
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

@bottle.get("/")
def prvi_zaslon():
    return bottle.template("zacetna_stran_tk.html")

@bottle.get("/rezultati/")
def rezultati_tekov():
    return bottle.template("rezultati.html")

@bottle.get("/kalkulator/")
def vrni_kalkulator():
    return bottle.template("kalkulator.html")

@bottle.get("/prijava/")
def vrni_prijavo():
    return bottle.template("prijava.html")

@bottle.get("/registracija/")
def registracija():
    return bottle.template("registracija.html")

@bottle.get("/statistika/")
def vrni_statistiko():
    return bottle.template("statistika.html", ime="Ioann", priimek="Stanković", starost="26", spol="moški")

# podatki se bodo prikazovali iz ene tabele vseh tekmovanj
# lahko naredimo potem html-je bolj genericne in ne vsakega posebej

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
    return bottle.template("2022_kranjski_10_M.html")

@bottle.get("/kraski22_10z/")
def kraski22_10z():
    return bottle.template("2022_kraski_10_Z.html")

@bottle.get("/blejski22_10z/")
def blejski22_m():
    return bottle.template("2022_blejski_Z.html")

@bottle.get("/ljub22_10z/")
def ljubljanski22_m():
    return bottle.template("2022_ljubljanski_10_Z.html")

@bottle.get("/kranj22_10z/")
def kranjski22_10m():
    return bottle.template("2022_kranjski_10_Z.html")

@bottle.get("/static/<filepath:path>")
def vrni_staticno_datoteko(filepath):
    return bottle.static_file(filepath, 'static')

bottle.run(reloader=True)