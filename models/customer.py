from dataclasses import dataclass
from typing import Optional


@dataclass
class Customer:
    id: int
    name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    vehicle_number: Optional[str] = None