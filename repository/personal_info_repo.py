from schema.personalInfo import PersonalInfo, PersonalInfoCreate, PersonalInfoUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_personal_info(new_personal_info: PersonalInfoCreate, db: db_dependency):
    db_personalInfo = PersonalInfo(**new_personal_info.dict())
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

    for key, value in updated_personal_info.dict(exclude_unset=True).items():
        setattr(db_personal_info, key, value)
    
    db.commit()
    return db_personal_info

def delete_personal_info(personalInfoId: int, db: db_dependency):
    db_personal_info = db.query(PersonalInfo).filter(PersonalInfo.personalInfoId == personalInfoId).first()

    db.delete(db_personal_info)
    db.commit()
    return {"message":"Personal Info Record Deleted Successfully."}