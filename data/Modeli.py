from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RangTekaca:
    id: int = field(default="")
    rang: str = field(default="")

@dataclass_json
@dataclass
class Uporabnik:
    uporabnisko_ime: str = field(default="")
    geslo_hash: str = field(default="")
    login: str = field(default="")
    spol: str = field(default="")
    datum_rojstva: str = field(default="")
    rang_tekaca: RangTekaca = field(default="")

@dataclass_json
@dataclass
class Cas:
    cas: str = field(default="")
    izbrano: bool = field(default=False)

@dataclass_json
@dataclass
class Razdalja:
    razdalja: int = field(default="")
    izbrano: bool = field(default=False)

@dataclass_json
@dataclass
class VrstaTeka:
    id: int = field(default="")
    vrsta: str = field(default="")

@dataclass_json
@dataclass
class Tek:
    id: int = field(default="")
    tekac: Uporabnik = field(default="")
    vrsta_teka: VrstaTeka = field(default="")
    razdalja: Razdalja = field(default="")
    cas: Cas = field(default="")

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
    tekmovanje: Tekmovanje = field(default="")
    priimek_ime: str = field(default="")
    rezultat: str = field(default="")
