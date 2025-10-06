from schema.honorMapping import HonorMapping, HonorMappingCreate, HonorMappingUpdate, HonorMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_honorMapping(new_honorMapping: HonorMappingCreate, db: db_dependency):
    db_honorMapping = HonorMapping(**new_honorMapping.dict())
    db.add(db_honorMapping)
    db.commit()
    return db_honorMapping

def get_honorMapping(db: db_dependency):
    honorMappings = db.query(HonorMapping).all()
    return honorMappings

def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingUpdate, db: db_dependency):
    db_honorMapping = db.query(HonorMapping).filter(honorMapping_id == HonorMapping.honorMappingId).first()

    if db_honorMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_honorMapping.dict(exclude_unset=True).items():
        setattr(db_honorMapping, key, value)
    
    db.commit()
    return db_honorMapping

def delete_honorMapping(honorMapping_id: int, honorMapping_delete: HonorMappingDelete, db: db_dependency):
    db_honorMapping = db.query(HonorMapping).filter(HonorMapping.honorMappingId == honorMapping_id).first()

    for key, value in honorMapping_delete.dict(exclude_unset=True).items():
        setattr(db_honorMapping, key, value)

    db.commit()
    return {"message":"Honor Mapping Record Deleted Successfully."}