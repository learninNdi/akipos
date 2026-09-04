from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Exchange:
    id: int
    exchange_datetime: datetime

    sale_id: Optional[int] = None
    customer_id: Optional[int] = None

    difference_amount: float = 0

    payment_method: Optional[str] = None
    note: Optional[str] = None

    created_by: Optional[int] = None