import bottle
import bottleext
# from model_tekaski import Parkirišče

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
    return bottle.template("2022_kraski_10_Zn.html")

@bottle.get("/blejski22_10z/")
def blejski22_m():
    return bottle.template("2022_blejski_Zn.html")

@bottle.get("/ljub22_10z/")
def ljubljanski22_m():
    return bottle.template("2022_ljubljanski_10_Z.html")

@bottle.get("/kranj22_10z/")
def kranjski22_10m():
    return bottle.template("2022_kranjski_10_Zn.html")

@bottle.get("/static/<filepath:path>")
def vrni_staticno_datoteko(filepath):
    return bottle.static_file(filepath, 'static')

bottle.run(reloader=True)