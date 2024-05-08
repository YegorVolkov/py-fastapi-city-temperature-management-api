from pydantic import BaseModel
from datetime import date


class TemperatureBase(BaseModel):
    city_name: str
    date_time_utc: date
    temperature: str


class Temperature(TemperatureBase):
    id: int

    class Config:
        from_attributes = True
