from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Uporabnik:
    username: str = field(default="")
    password_hash: str = field(default="")
    last_login: str = field(default="")

@dataclass
class Rezultat:
    id: int = field(default=0)
    uvrstitev: int = field(default=0)
