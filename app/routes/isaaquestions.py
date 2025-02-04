from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.oauth2 import get_current_user
from app import schemas, models


router = APIRouter()
@router.post("/patients/isaa_questions", response_model=schemas.IsaaQuestions)
async def isaa_questions(patient_isaa: schemas.IsaaQuestions, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    
    print(current_user.id)

    latest_patient = db.query(models.PatientClinicalProfile).filter(models.PatientClinicalProfile.user_id == current_user.id).order_by(models.PatientClinicalProfile.created_at.desc()).first()

    if not latest_patient:
        raise HTTPException(status_code=404, detail="No patient found for the current user")

    new_patient_isaa = models.ISAAQuestions(
        name = patient_isaa.name,
        poor_eye_contact = patient_isaa.poor_eye_contact, 
        lacks_social_smile = patient_isaa.lacks_social_smile,
        remains_aloof = patient_isaa.remains_aloof,
        does_not_reach_out_to_others = patient_isaa.does_not_reach_out_to_others,
        unable_to_relate_to_people = patient_isaa.unable_to_relate_to_people,
        unable_to_respond_to_cues = patient_isaa.unable_to_respond_to_cues,
        solitary_repetitive_play = patient_isaa.solitary_repetitive_play,
        unable_to_take_turns = patient_isaa.unable_to_take_turns,
        does_not_maintain_peer_relationships = patient_isaa.does_not_maintain_peer_relationships,
        inappropriate_emotional_response = patient_isaa.inappropriate_emotional_response,
        exaggerated_emotions = patient_isaa.exaggerated_emotions,
        self_stimulating_emotions = patient_isaa.self_stimulating_emotions,
        lacks_fear_of_danger = patient_isaa.lacks_fear_of_danger,
        excited_for_no_reason = patient_isaa.excited_for_no_reason,
        acquired_speech_lost = patient_isaa.acquired_speech_lost,
        difficulty_nonverbal_language = patient_isaa.difficulty_nonverbal_language,
        repetitive_language_use = patient_isaa.repetitive_language_use,
        echolalic_speech = patient_isaa.echolalic_speech,
        unusual_noises = patient_isaa.unusual_noises,
        unable_to_sustain_conversation = patient_isaa.unable_to_sustain_conversation,
        repetitive_motor_mannerisms = patient_isaa.repetitive_motor_mannerisms,
        attachment_to_objects = patient_isaa.attachment_to_objects,
        hyperactivity_restlessness = patient_isaa.hyperactivity_restlessness,
        aggressive_behavior = patient_isaa.aggressive_behavior,
        temper_tantrums = patient_isaa.temper_tantrums,
        self_injurious_behavior = patient_isaa.self_injurious_behavior,
        insists_on_sameness = patient_isaa.insists_on_sameness,
        sensitive_to_sensory_stimuli = patient_isaa.sensitive_to_sensory_stimuli,
        stares_into_space = patient_isaa.stares_into_space,
        difficulty_tracking_objects = patient_isaa.difficulty_tracking_objects,
        unusual_vision = patient_isaa.unusual_vision,
        insensitive_to_pain = patient_isaa.insensitive_to_pain,
        unusual_response_to_objects_people = patient_isaa.unusual_response_to_objects_people,
        inconsistent_attention = patient_isaa.inconsistent_attention,
        delay_in_responding = patient_isaa.delay_in_responding,
        unusual_memory = patient_isaa.unusual_memory,
        savant_ability = patient_isaa.savant_ability,
        patient_id = latest_patient.id,
    )

    try:
        db.add(new_patient_isaa)
        db.commit()
        db.refresh(new_patient_isaa)
        return new_patient_isaa
    except Exception as e:
        db.rollback()  
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



@router.get("/patients/isaa_questions_details/{patient_issa_id}", response_model=schemas.IsaaQuestions)
async def get_patient_isaa(patient_issa_id:int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_patients_isaa = db.query(models.ISAAQuestions).filter(models.ISAAQuestions.patient_id == patient_issa_id).first()

    if not db_patients_isaa :
        raise HTTPException(status_code=404, detail="No patients exist")

    return db_patients_isaa

@router.get("/patients/{patient_name}/issa", response_model=schemas.IsaaQuestions)
async def get_patient_profile(patient_name: str, db: Session = Depends(get_db)):
    patient = db.query(models.ISAAQuestions).filter(models.ISAAQuestions.name == patient_name).first()
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return patient
