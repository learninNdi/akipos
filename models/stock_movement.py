from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class StockMovement:
    id: int
    product_id: str
    movement_datetime: datetime

    movement_type: str
    quantity: int

    stock_before: int
    stock_after: int

    reference_type: Optional[str] = None
    reference_id: Optional[int] = None

    note: Optional[str] = None
    created_by: Optional[int] = None