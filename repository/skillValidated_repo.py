from schema.skillValidated import SkillValidated, SkillValidatedCreate, SkillValidatedUpdate, SkillValidatedDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_skillValidated(new_skillValidated: SkillValidatedCreate, db: db_dependency):
    db_skillValidated = SkillValidated(**new_skillValidated.dict())
    db.add(db_skillValidated)
    db.commit()
    return db_skillValidated

def get_skillValidated(db: db_dependency):
    skillValidated = db.query(SkillValidated).all()
    return skillValidated

def update_skillValidated(skillValidated_id: int, updated_skillValidated: SkillValidatedUpdate, db: db_dependency):
    db_skillValidated = db.query(SkillValidated).filter(skillValidated_id == SkillValidated.skillValidatedId).first()

    if db_skillValidated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_skillValidated.dict(exclude_unset=True).items():
        setattr(db_skillValidated, key, value)
    
    db.commit()
    return db_skillValidated

def delete_skillValidated(skillValidated_id: int, skillValidated_delete: SkillValidatedDelete, db: db_dependency):
    db_skillValidated = db.query(SkillValidated).filter(SkillValidated.skillValidatedId == skillValidated_id).first()

    for key, value in skillValidated_delete.dict(exclude_unset=True).items():
        setattr(db_skillValidated, key, value)
         
    db.commit()
    return {"message":"Skill Validated Record Deleted Successfully."}