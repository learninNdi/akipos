from dataclasses import dataclass
from datetime import datetime


@dataclass
class InventoryLayer:
    id: int
    product_id: str
    purchase_item_id: int

    original_quantity: int
    remaining_quantity: int

    unit_cost: float
    created_at: datetime