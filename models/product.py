from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    item_id: str
    item_name: str

    voltage: Optional[str] = None
    capacity: Optional[str] = None
    cca: Optional[str] = None

    weight: Optional[float] = None
    dimension: Optional[str] = None

    minimum_margin: float = 0
    selling_price: float = 0
    quantity: int = 0

    note: Optional[str] = None