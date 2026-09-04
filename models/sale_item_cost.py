from dataclasses import dataclass


@dataclass
class SaleItemCost:
    id: int
    sale_item_id: int
    inventory_layer_id: int

    quantity: int
    cost_price: float

    @property
    def total_cost(self) -> float:
        return self.quantity * self.cost_price