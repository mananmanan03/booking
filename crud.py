from sqlalchemy.orm import Session
from models import Booking
from schemas import BookingCreate

def create_booking(db:Session, booking:BookingCreate):
    db_booking=Booking(
        customer_name=booking.customer_name,
        booking_date=booking.booking_date,
        amount=booking.amount,
        vendor_details=booking.vendor_details,
        )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def get_booking(db:Session, booking_id:int):
    return db.query(Booking).filter(Booking.id==booking_id).first()

def get_bookings(db:Session, skip:int=0, limit: int=10 ):
    return db.query(Booking).offset(skip).limit(limit).all()

def delete_booking(db:Session, booking_id:int):
    booking=db.query(Booking).filter(Booking.id==booking_id).first()
    if booking:
        db.delete(booking)
        db.commit()
    
    return booking