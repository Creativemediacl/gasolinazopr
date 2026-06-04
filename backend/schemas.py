from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PriceCreate(BaseModel):
    station_name: str
    municipality: str
    fuel_type: str
    price: float

class PriceResponse(BaseModel):
    id: int
    station_name: str
    municipality: str
    fuel_type: str
    price: float
    reported_at: datetime
    is_outdated: bool
    thumbs_up: int
    thumbs_down: int

    class Config:
        from_attributes = True
