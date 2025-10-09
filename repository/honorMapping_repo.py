from schema.honorMapping import HonorMapping, HonorMappingBase, HonorMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_honorMapping(new_honorMapping: HonorMappingBase, db: db_dependency, currentUser):
    db_honorMapping = HonorMapping(**new_honorMapping.model_dump(), createdBy = currentUser["userId"])
    db.add(db_honorMapping)
    db.commit()
    return db_honorMapping

def get_honorMapping(db: db_dependency):
    honorMappings = db.query(HonorMapping).all()
    return honorMappings

def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingBase, db: db_dependency, currentUser):
    db_honorMapping = db.query(HonorMapping).filter(honorMapping_id == HonorMapping.honorMappingId).first()

    if db_honorMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_honorMapping.model_dump().items():
        setattr(db_honorMapping, key, value)

    db_honorMapping.changedBy = currentUser["userId"]
    
    db.commit()
    return db_honorMapping

def delete_honorMapping(honorMapping_id: int, honorMapping_delete: HonorMappingDelete, db: db_dependency, currentUser):
    db_honorMapping = db.query(HonorMapping).filter(HonorMapping.honorMappingId == honorMapping_id).first()

    for key, value in honorMapping_delete.model_dump().items():
        setattr(db_honorMapping, key, value)

    db_honorMapping.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"Honor Mapping Record Deleted Successfully."}