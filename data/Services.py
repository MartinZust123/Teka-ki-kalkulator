from Database import Repo
from Modeli import *

#from data.Database import Repo
#from data.Modeli import *
from typing import Dict
from re import sub
import dataclasses
import bcrypt
from typing import Type, Union
from datetime import date

class AuthService:

    repo : Repo
    def __init__(self, repo : Repo):
        
        self.repo = repo

    def obstaja_uporabnik(self, uporabnik: str) -> bool:
        try:
            user = self.repo.dobi_gen_id(Uporabnik, uporabnik, id_col="username")
            return True
        except:
            return False

    def prijavi_uporabnika(self, uporabnik : str, geslo: str) -> Union[UporabnikDto,bool] :

        # Najprej dobimo uporabnika iz baze
        user = self.repo.dobi_gen_id(Uporabnik, uporabnik, id_col="username")

        geslo_bytes = geslo.encode('utf-8')
        # Ustvarimo hash iz gesla, ki ga je vnesel uporabnik
        succ = bcrypt.checkpw(geslo_bytes, user.geslo.encode('utf-8'))

        if succ:
            # popravimo last login time
            #user.last_login = date.today().isoformat()
            #self.repo.posodobi_gen(user, id_col="username")
            return UporabnikDto(username=user.username, id=user.id)
        
        return False


    def dodaj_uporabnika(self, username: str, imeinpriimek: str, geslo: str, spol: str, leto: int ) -> UporabnikDto:

        # zgradimo hash za geslo od uporabnika

        # Najprej geslo zakodiramo kot seznam bajtov
        bytes = geslo.encode('utf-8')
  
        # Nato ustvarimo salt
        salt = bcrypt.gensalt()
        
        # In na koncu ustvarimo hash gesla
        password_hash = bcrypt.hashpw(bytes, salt)

        # Sedaj ustvarimo objekt Uporabnik in ga zapišemo bazo

        uporabnik = Uporabnik(
            username = username,
            imeinpriimek = imeinpriimek,
            geslo = password_hash.decode(),
            spol= spol,
            starost= leto
        )

        self.repo.dodaj_gen(uporabnik)

        return UporabnikDto(username=username, id=uporabnik.id)