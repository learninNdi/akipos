from dataclasses import dataclass


@dataclass
class ExchangeItem:
    id: int
    exchange_id: int

    product_id: str
    quantity: int

    direction: str
    unit_price: float