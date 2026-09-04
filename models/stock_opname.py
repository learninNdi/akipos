from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class StockOpname:
    id: int
    opname_datetime: datetime

    note: Optional[str] = None
    created_by: Optional[int] = None