from schema.skillValidatedMapping import SkillValidatedMapping, SkillValidatedMappingBase, SkillValidatedMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_skillValidatedMapping(new_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, currentUser):
    db_skillValidatedMapping = SkillValidatedMapping(**new_skillValidatedMapping.model_dump(), createdBy = currentUser["userId"])
    db.add(db_skillValidatedMapping)
    db.commit()
    return db_skillValidatedMapping

def get_skillValidatedMapping(db: db_dependency):
    skillValidatedMappings = db.query(SkillValidatedMapping).all()
    return skillValidatedMappings

def update_skillValidatedMapping(skillValidatedMapping_id: int, updated_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, currentUser):
    db_skillValidatedMapping = db.query(SkillValidatedMapping).filter(skillValidatedMapping_id == SkillValidatedMapping.skillValidatedMappingId).first()

    if db_skillValidatedMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_skillValidatedMapping.model_dump().items():
        setattr(db_skillValidatedMapping, key, value)

    db_skillValidatedMapping.changedBy = currentUser["userId"]
    
    db.commit()
    return db_skillValidatedMapping

def delete_skillValidatedMapping(skillValidatedMapping_id: int, skillValidatedMapping_delete: SkillValidatedMappingDelete, db: db_dependency, currentUser):
    db_skillValidatedMapping = db.query(SkillValidatedMapping).filter(SkillValidatedMapping.skillValidatedMappingId == skillValidatedMapping_id).first()

    for key, value in skillValidatedMapping_delete.model_dump().items():
        setattr(db_skillValidatedMapping, key, value)  

    db_skillValidatedMapping.deletedBy = currentUser["userId"]  
        
    db.commit()
    return {"message":"Skill Validated Mapping Record Deleted Successfully."}