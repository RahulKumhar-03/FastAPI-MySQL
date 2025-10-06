from schema.awardMapping import AwardMapping, awardMappingCreate, AwardMappingUpdate, AwardMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_awardMapping(new_awardMapping: awardMappingCreate, db: db_dependency):
    db_awardMapping = AwardMapping(**new_awardMapping.dict())
    db.add(db_awardMapping)
    db.commit()
    return db_awardMapping

def get_awardMapping(db: db_dependency):
    awardMappings = db.query(AwardMapping).all()
    return awardMappings

def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingUpdate, db: db_dependency):
    db_awardMapping = db.query(AwardMapping).filter(awardMapping_id == AwardMapping.awardMappingId).first()

    if db_awardMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_awardMapping.dict(exclude_unset=True).items():
        setattr(db_awardMapping, key, value)
    
    db.commit()
    return db_awardMapping

def delete_awardMapping(awardMapping_id: int, awardMapping_delete: AwardMappingDelete, db: db_dependency):
    db_awardMapping = db.query(AwardMapping).filter(AwardMapping.awardMappingId == awardMapping_id).first()

    for key, value in awardMapping_delete.dict(exclude_unset=True).items():
        setattr(db_awardMapping, key, value)

    db.commit()
    return {"message":"Award Mapping Record Deleted Successfully."}