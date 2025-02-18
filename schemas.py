from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    customer_name: str
    booking_date: datetime
    amount: float
    vendor_details: str

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id:int
    
    class Config:
        orm_mode=True