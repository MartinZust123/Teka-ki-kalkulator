import bottle
import bottleext
# from model_tekaski import Parkirišče

@bottle.get("/")
def prvi_zaslon():
    return bottle.template("views/zacetna_stran_tk.html")

@bottle.get("/rezultati/")
def rezultati_tekov():
    return bottle.template("views/rezultati.html")

@bottle.get("/kalkulator/")
def vrni_kalkulator():
    return bottle.template("views/kalkulator.html")

bottle.run(reloader=True)