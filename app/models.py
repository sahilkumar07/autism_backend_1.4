from sqlalchemy import TIMESTAMP, Boolean, Column, Date, ForeignKey, Integer, String, Text, func, text, BigInteger
from sqlalchemy.sql.expression import null
from .database import Base 
from sqlalchemy.orm import relationship


class User(Base) :
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    patients_cp = relationship("PatientClinicalProfile", back_populates="user_cp")
    # patients_isaa = relationship("ISAAQuestions", back_populates="user_isaa")



class PatientClinicalProfile(Base):
    __tablename__ = "patient_clinical_profile"


    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    dob = Column(Date, nullable=False)
    sex = Column(String, nullable=False)  
    contact = Column(BigInteger, unique=True, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    fullTermDelivery = Column(String, nullable=False)  
    deliveryType = Column(String, nullable=False)  
    birthCry = Column(String, nullable=False)  

    malnutrition_in_mother = Column(String, default=False)
    high_blood_sugar_in_mother = Column(String, default=False)
    high_blood_pressure_in_mother = Column(String, default=False)
    fall_injury_in_mother = Column(String, default=False)
    tobacco_exposure_in_mother = Column(String, default=False)
    alcohol_drug_abuse_in_mother = Column(String, default=False)
    infection_fever_in_mother = Column(String, default=False)
    psychological_stress_in_mother = Column(String, default=False)
    hypothyroidism_in_mother = Column(String, default=False)

    infection = Column(String, default=False)
    fever = Column(String, default=False)
    seizure = Column(String, default=False)
    oxygen_insufficiency = Column(String, default=False)
    jaundice = Column(String, default=False)
    high_fever = Column(String, default=False)
    head_injury = Column(String, default=False)

    familyHistory = Column(Text, nullable=True)
    diagnosisKnowledge = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())


    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_cp = relationship("User", back_populates="patients_cp")



class ISAAQuestions(Base):
    __tablename__ = "isaa"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    poor_eye_contact = Column(String)
    lacks_social_smile = Column(String)
    remains_aloof = Column(String)
    does_not_reach_out_to_others = Column(String)
    unable_to_relate_to_people = Column(String)
    unable_to_respond_to_cues = Column(String)
    solitary_repetitive_play = Column(String)
    unable_to_take_turns = Column(String)
    does_not_maintain_peer_relationships = Column(String)
    inappropriate_emotional_response = Column(String)
    exaggerated_emotions = Column(String)
    self_stimulating_emotions = Column(String)
    lacks_fear_of_danger = Column(String)
    excited_for_no_reason = Column(String)
    acquired_speech_lost = Column(String)
    difficulty_nonverbal_language = Column(String)
    repetitive_language_use = Column(String)
    echolalic_speech = Column(String)
    unusual_noises = Column(String)
    unable_to_sustain_conversation = Column(String)
    repetitive_motor_mannerisms = Column(String)
    attachment_to_objects = Column(String)
    hyperactivity_restlessness = Column(String)
    aggressive_behavior = Column(String)
    temper_tantrums = Column(String)
    self_injurious_behavior = Column(String)
    insists_on_sameness = Column(String)
    sensitive_to_sensory_stimuli = Column(String)
    stares_into_space = Column(String)
    difficulty_tracking_objects = Column(String)
    unusual_vision = Column(String)
    insensitive_to_pain = Column(String)
    unusual_response_to_objects_people = Column(String)
    inconsistent_attention = Column(String)
    delay_in_responding = Column(String)
    unusual_memory = Column(String)
    savant_ability = Column(String)
    patient_id = Column(Integer)







