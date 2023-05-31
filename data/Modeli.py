from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Uporabnik:
    uporabnisko_ime: str = field(default="")
    geslo_hash: str = field(default="")
    login: str = field(default="")
    spol: str = field(default="")
    datum_rojstva: str = field(default="")
    rang_tekaca: str = field(default="")

@dataclass_json
@dataclass
class Tek:
    id: int = field(default="")
    vrsta_teka: str = field(default="")
    razdalja: int = field(default="")
    cas: int = field(default="")

@dataclass_json
@dataclass
class Tekmovanje:
    id: int = field(default="")
    naziv: str = field(default="")
    leto: int = field(default="")
    razdalja: int = field(default="")

@dataclass_json
@dataclass
class Rezultat:
    id: int = field(default="")
    tekmovanje = str = field(default="")
    priimek_ime: str = field(default="")
    rezultat: str = field(default="")


