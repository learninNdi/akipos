from dataclasses import dataclass
from typing import Optional


@dataclass
class Supplier:
    id: int
    name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    note: Optional[str] = None