from dataclasses import dataclass


@dataclass
class SaleItem:
    id: int
    sale_id: int
    product_id: str

    quantity: int
    unit_price: float

    @property
    def line_total(self) -> float:
        return self.quantity * self.unit_price