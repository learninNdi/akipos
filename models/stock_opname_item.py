from dataclasses import dataclass
from typing import Optional


@dataclass
class StockOpnameItem:
    id: int
    stock_opname_id: int
    product_id: str

    system_quantity: int
    actual_quantity: int

    note: Optional[str] = None

    @property
    def difference(self) -> int:
        return self.actual_quantity - self.system_quantity