from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Purchase:
    id: int
    purchase_datetime: datetime
    supplier_id: Optional[int] = None
    total: float = 0
    note: Optional[str] = None