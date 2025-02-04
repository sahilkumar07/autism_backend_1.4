import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from pydantic import conint
from sqlalchemy import Integer


class UserResponse(BaseModel) :
    id : int
    firstName : str
    lastName : str  
    email : EmailStr
    phone: str

    class Config :
        from_attributes = True


class UserCreate(BaseModel) :
    firstName : str
    lastName : str
    phone : str
    email : EmailStr 
    password : str


class UserLogin(BaseModel) :
    email : EmailStr
    password : str


class Token(BaseModel) :
    access_token : str
    token_type : str


class TokenData(BaseModel) :
    id : Optional[str] = None


class PatientClinicalProfile(BaseModel):
    name: str
    age: int
    dob: datetime.date
    sex: str
    contact: int
    height: int
    weight: int
    fullTermDelivery: str
    deliveryType: str
    birthCry: str

    malnutrition_in_mother: Optional[str] = None
    high_blood_sugar_in_mother: Optional[str] = None
    high_blood_pressure_in_mother: Optional[str] = None
    fall_injury_in_mother: Optional[str] = None
    tobacco_exposure_in_mother: Optional[str] = None
    alcohol_drug_abuse_in_mother: Optional[str] = None
    infection_fever_in_mother: Optional[str] = None
    psychological_stress_in_mother: Optional[str] = None
    hypothyroidism_in_mother: Optional[str] = None

    infection: Optional[str] = None
    fever: Optional[str] = None
    seizure: Optional[str] = None
    oxygen_insufficiency: Optional[str] = None
    jaundice: Optional[str] = None
    high_fever: Optional[str] = None
    head_injury: Optional[str] = None

    familyHistory: Optional[str] = None
    diagnosisKnowledge: Optional[str] = None

    class Config:
        orm_mode = True


class IsaaQuestions(BaseModel):

    name: str
    poor_eye_contact: str
    lacks_social_smile: str
    remains_aloof: str
    does_not_reach_out_to_others: str
    unable_to_relate_to_people: str
    unable_to_respond_to_cues: str
    solitary_repetitive_play: str
    unable_to_take_turns: str
    does_not_maintain_peer_relationships: str
    inappropriate_emotional_response: str
    exaggerated_emotions: str
    self_stimulating_emotions: str
    lacks_fear_of_danger: str
    excited_for_no_reason: str
    acquired_speech_lost: str
    difficulty_nonverbal_language: str
    repetitive_language_use: str
    echolalic_speech: str
    unusual_noises: str
    unable_to_sustain_conversation: str
    repetitive_motor_mannerisms: str
    attachment_to_objects: str
    hyperactivity_restlessness: str
    aggressive_behavior: str
    temper_tantrums: str
    self_injurious_behavior: str
    insists_on_sameness: str
    sensitive_to_sensory_stimuli: str
    stares_into_space: str
    difficulty_tracking_objects: str
    unusual_vision: str
    insensitive_to_pain: str
    unusual_response_to_objects_people: str
    inconsistent_attention: str
    delay_in_responding: str
    unusual_memory: str
    savant_ability: str
    # patient_id: Integer

class DoctorWithPatients(BaseModel):
    id:int
    firstName: str
    lastName: str
    phone: int
    email: str
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
    
