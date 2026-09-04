from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Sale:
    id: int
    sale_datetime: datetime

    subtotal: float
    total: float

    customer_id: Optional[int] = None
    payment_method: str = "CASH"

    note: Optional[str] = None
    created_by: Optional[int] = None