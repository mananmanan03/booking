from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.post("/bookings/",response_model=schemas.Booking)
def create_booking(booking:schemas.Booking, db:Session=Depends(get_db)):
    return crud.create_booking(db=db,booking=booking)
    
@app.get("/bookings/{booking_id}",response_model=schemas.Booking)
def read_booking(booking_id :int, db:Session=Depends(get_db)):
    db_booking=crud.get_booking(db,booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking
    
@app.get("/bookings/",response_model=schemas.Booking)
def read_bookings(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    bookings=crud.get_bookings(db,skip=skip,limit=limit)
    return bookings
    
@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id:int, db:Session=Depends(get_db)):
    result=crud.delete_booking(db,booking_id=booking_id)
    if result:
        return {"msg":"Booking deleted successfully"}
    raise HTTPException(status_code=404,detail="Booking not found")
