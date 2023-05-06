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

@bottle.get("/static/<filepath:path>")
def vrni_staticno_datoteko(filepath):
    return bottle.static_file(filepath, 'static')


bottle.run(reloader=True)