from sqlalchemy import Column, Integer, String, Float, DateTime
from database import basestring


class Booking(Base):
    __tablename="bookings"
    
    id=Column(Integer, primary_key=True, index=True)
    customer_name=Column(String, nullable=False)
    booking_date=Column(DateTime, nullable=False)
    amount=Column(Float, nullable=False)
    vendor_details=Column(String, nullable=False)