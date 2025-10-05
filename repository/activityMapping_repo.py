from schema.activityMapping import ActivityMapping, ActivityMappingCreate, ActivityMappingUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_activityMapping(new_activityMapping: ActivityMappingCreate, db: db_dependency):
    db_activityMapping = ActivityMapping(**new_activityMapping.dict())
    db.add(db_activityMapping)
    db.commit()
    return db_activityMapping

def get_activityMapping(db: db_dependency):
    activityMappings = db.query(ActivityMapping).all()
    return activityMappings

def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingUpdate, db: db_dependency):
    db_activityMapping = db.query(ActivityMapping).filter(activityMapping_id == ActivityMapping.activityMappingId).first()

    if db_activityMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_activityMapping.dict(exclude_unset=True).items():
        setattr(db_activityMapping, key, value)
    
    db.commit()
    return db_activityMapping

def delete_activityMapping(activityMapping_id: int, db: db_dependency):
    db_activityMapping = db.query(ActivityMapping).filter(ActivityMapping.activityMappingId == activityMapping_id).first()

    db.delete(db_activityMapping)
    db.commit()
    return {"message":"Activity Mapping Record Deleted Successfully."}