from pydantic import BaseModel, Field
from datetime import date as date_


class BestOfferBase(BaseModel):
    date: date_ = Field(...)
    offer: str = Field(...)
    url: str =  Field(...)
    price: int = Field(...)

class BestOfferRead(BestOfferBase):
    id: int = Field(...)
    class Config:
        from_attributes = True