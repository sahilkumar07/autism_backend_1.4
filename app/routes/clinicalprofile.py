from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.oauth2 import get_current_user
from app import schemas, models
# from .dependencies import get_current_user  # Dependency to get the current authenticated user

router = APIRouter()


@router.post("/patients/clinical_profile", response_model=schemas.PatientClinicalProfile)
async def create_patient_profile(patient: schemas.PatientClinicalProfile, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    existing_patient = db.query(models.PatientClinicalProfile).filter(models.PatientClinicalProfile.contact == patient.contact).first()
    if existing_patient:
        raise HTTPException(status_code=400, detail="Patient with this contact already exists.")
    
    
    new_patient = models.PatientClinicalProfile(
        name=patient.name,
        age=patient.age,
        dob=patient.dob,
        sex=patient.sex,
        contact=patient.contact,
        height=patient.height,
        weight=patient.weight,
        fullTermDelivery=patient.fullTermDelivery,
        deliveryType=patient.deliveryType,
        birthCry=patient.birthCry,
        malnutrition_in_mother=patient.malnutrition_in_mother,
        high_blood_sugar_in_mother=patient.high_blood_sugar_in_mother,
        high_blood_pressure_in_mother=patient.high_blood_pressure_in_mother,
        fall_injury_in_mother=patient.fall_injury_in_mother,
        tobacco_exposure_in_mother=patient.tobacco_exposure_in_mother,
        alcohol_drug_abuse_in_mother=patient.alcohol_drug_abuse_in_mother,
        infection_fever_in_mother=patient.infection_fever_in_mother,
        psychological_stress_in_mother=patient.psychological_stress_in_mother,
        hypothyroidism_in_mother=patient.hypothyroidism_in_mother,
        infection=patient.infection,
        fever=patient.fever,
        seizure=patient.seizure,
        oxygen_insufficiency=patient.oxygen_insufficiency,
        jaundice=patient.jaundice,
        high_fever=patient.high_fever,
        head_injury=patient.head_injury,
        familyHistory=patient.familyHistory,
        diagnosisKnowledge=patient.diagnosisKnowledge,
        user_id=current_user.id
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

# # Route to retrieve all patient clinical profile information for the current user
@router.get("/patients/clinical_profiles/", response_model=List[schemas.PatientClinicalProfile])
async def get_patient_profiles(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # Retrieve the patient's clinical profiles of the current user
    db_patients = db.query(models.PatientClinicalProfile).filter(models.PatientClinicalProfile.user_id == current_user.id).all()

    if not db_patients :
        raise HTTPException(status_code=404, detail="No patients exist")
    
    return db_patients

@router.get("/doctors/{doctor_id}/patients", response_model=List[schemas.PatientClinicalProfile])
async def get_patients_for_doctor(doctor_id: int, db: Session = Depends(get_db)):
    # Confirm the doctor exists first
    doctor = db.query(models.User).filter(models.User.id == doctor_id).first()
    print(doctor)
    if not doctor:
        raise HTTPException(status_code=400, detail=f"Doctor with ID {doctor_id} not found")
    
    # If the doctor exists, fetch the associated patients
    db_patients = db.query(models.PatientClinicalProfile).filter(models.PatientClinicalProfile.user_id == doctor_id).all()
    print(db_patients)
    if not db_patients:
        raise HTTPException(status_code=404, detail=f"No patients found for doctor with ID {doctor_id}")
    
    return db_patients

@router.get("/patients/{patient_name}/profile", response_model=schemas.PatientClinicalProfile)
async def get_patient_profile(patient_name: str, db: Session = Depends(get_db)):
    patient = db.query(models.PatientClinicalProfile).filter(models.PatientClinicalProfile.name == patient_name).first()
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return patient





