from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.get("/doctors", response_model=List[schemas.DoctorWithPatients])
async def get_doctors(db: Session = Depends(get_db)):
    doctors = db.query(models.User).all()
    if not doctors:
        raise HTTPException(status_code=404, detail="No doctors found")
    for doctor in doctors:
        doctor.phone = str(doctor.phone)
    return doctors
