from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class RangTekaca:
    id: int = field(default=0)
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
    cas: str = field(default=0)
    izbrano: bool = field(default=False)

@dataclass_json
@dataclass
class Razdalja:
    razdalja: int = field(default=0)
    izbrano: bool = field(default=False)

@dataclass_json
@dataclass
class VrstaTeka:
    id: int = field(default=0)
    vrsta: str = field(default="")

@dataclass_json
@dataclass
class Tek:
    id: int = field(default=0)
    tekac: Uporabnik = field(default="")
    vrsta_teka: VrstaTeka = field(default="")
    razdalja: Razdalja = field(default="")
    cas: Cas = field(default="")

@dataclass_json
@dataclass
class Tekmovanje:
    id: int = field(default=0)
    naziv: str = field(default="")
    leto: int = field(default=0)
    razdalja: int = field(default="")

@dataclass_json
@dataclass
class Rezultat:
    id: int = field(default=0)
    tekmovanje: Tekmovanje = field(default="")
    priimek_ime: str = field(default="")
    rezultat: str = field(default="")
