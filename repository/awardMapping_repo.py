from schema.awardMapping import AwardMapping, AwardMappingBase, AwardMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_awardMapping(new_awardMapping: AwardMappingBase, db: db_dependency, currentUser):
    db_awardMapping = AwardMapping(
        **new_awardMapping.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_awardMapping)
    db.commit()
    return db_awardMapping

def get_awardMapping(db: db_dependency):
    awardMappings = db.query(AwardMapping).all()
    return awardMappings

def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingBase, db: db_dependency, currentUser):
    db_awardMapping = db.query(AwardMapping).filter(awardMapping_id == AwardMapping.awardMappingId).first()

    if db_awardMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_awardMapping.model_dump().items():
        setattr(db_awardMapping, key, value)

    db_awardMapping.changedBy = currentUser["userId"]
    
    db.commit()
    return db_awardMapping

def delete_awardMapping(awardMapping_id: int, awardMapping_delete: AwardMappingDelete, db: db_dependency, currentUser):
    db_awardMapping = db.query(AwardMapping).filter(AwardMapping.awardMappingId == awardMapping_id).first()

    for key, value in awardMapping_delete.model_dump().items():
        setattr(db_awardMapping, key, value)

    db_awardMapping.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"Award Mapping Record Deleted Successfully."}