from schema.activityMapping import ActivityMapping, ActivityMappingBase, ActivityMappingDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_activityMapping(new_activityMapping: ActivityMappingBase, db: db_dependency, currentUser):
    db_activityMapping = ActivityMapping(
        **new_activityMapping.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_activityMapping)
    db.commit()
    return db_activityMapping

def get_activityMapping(db: db_dependency):
    activityMappings = db.query(ActivityMapping).all()
    return activityMappings

def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingBase, db: db_dependency, currentUser):
    db_activityMapping = db.query(ActivityMapping).filter(activityMapping_id == ActivityMapping.activityMappingId).first()

    if db_activityMapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_activityMapping.model_dump().items():
        setattr(db_activityMapping, key, value)

    db_activityMapping.changedBy = currentUser["userId"]
    
    db.commit()
    return db_activityMapping

def delete_activityMapping(activityMapping_id: int, activity_delete: ActivityMappingDelete, db: db_dependency, currentUser):
    db_activityMapping = db.query(ActivityMapping).filter(ActivityMapping.activityMappingId == activityMapping_id).first()

    for key, value in activity_delete.model_dump().items():
        setattr(db_activityMapping, key, value)

    db_activityMapping.deletedBy = currentUser["userId"]
        
    db.commit()
    return {"message":"Activity Mapping Record Deleted Successfully."}