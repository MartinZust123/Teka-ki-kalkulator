from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Uporabnik:
    id: int = field(default=0)
    username: str = field(default="")
    imeinpriimek: str = field(default="")
    geslo: str = field(default="")
    spol: str = field(default="")
    starost: int = field(default=0)

@dataclass_json
@dataclass
class UporabnikDto:
    id: int = field(default=0)
    username: str = field(default="")

@dataclass_json
@dataclass
class Rezultat: 
    id: int = field(default=0)
    spol: str = field(default="")
    priimekinime: str = field(default="")
    lr: int = field(default=0)
    
    kraj: str = field(default="")
    leto: int = field(default=0)
    razdalja: int = field(default=0)

    km_dva: str = field(default="")
    km_tri: str = field(default="")
    km_tt: str = field(default="")
    km_pet: str = field(default="")
    km_sest: str = field(default="")
    km_ss: str = field(default="")
    km_deset: str = field(default="")
    km_petnajst: str = field(default="")
    km_sedemnajst: str = field(default="")
    km_dvajset: str = field(default="")
    km_enaindvajset: str = field(default="")
    km_polmaraton: str = field(default="")
    km_petindvajset: str = field(default="")
    km_trideset: str = field(default="")
    km_petintrideset: str = field(default="")
    km_stirideset: str = field(default="")
    km_maraton: str = field(default="")

    

    

@dataclass_json
@dataclass
class Tek:
    id: int = field(default=0)
    tekac: str = field(default="")
    datum: str = field(default="")
#    vrsta_teka: str = field(default="")
    razdalja: int = field(default=0)
    cas: int = field(default=0)

