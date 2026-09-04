from dataclasses import dataclass


@dataclass
class PurchaseItem:
    id: int
    purchase_id: int
    product_id: str
    quantity: int
    unit_cost: float

    @property
    def total_cost(self) -> float:
        return self.quantity * self.unit_cost