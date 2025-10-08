from schema.personalInfo import PersonalInfo, PersonalInfoCreate, PersonalInfoUpdate, PersonalInfoDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_personal_info(new_personal_info: PersonalInfoCreate, db: db_dependency):
    db_personalInfo = PersonalInfo(**new_personal_info.model_dump())
    db.add(db_personalInfo)
    db.commit()
    return db_personalInfo

def get_personal_infos(db: db_dependency):
    personalInfos = db.query(PersonalInfo).all()
    return personalInfos

def update_personal_info(personal_info_id: int, updated_personal_info: PersonalInfoUpdate, db: db_dependency):
    db_personal_info = db.query(PersonalInfo).filter(personal_info_id == PersonalInfo.personalInfoId).first()

    if db_personal_info is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_personal_info.model_dump().items():
        setattr(db_personal_info, key, value)
    
    db.commit()
    return db_personal_info

def delete_personal_info(personalInfoId: int, personalInfo_delete: PersonalInfoDelete, db: db_dependency):
    db_personal_info = db.query(PersonalInfo).filter(PersonalInfo.personalInfoId == personalInfoId).first()

    for key, value in personalInfo_delete.model_dump().items():
        setattr(db_personal_info, key, value)
        
    db.commit()
    return {"message":"Personal Info Record Deleted Successfully."}