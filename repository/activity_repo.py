from schema.activity import Activity, ActivityUpdate, ActivityCreate, ActivityDelete
from database import db_dependency
from fastapi import HTTPException, status

def create_activity(new_activity: ActivityCreate, db: db_dependency):
    db_activity = Activity(**new_activity.model_dump())
    db.add(db_activity)
    db.commit()
    return db_activity

def get_activitys(db: db_dependency):
    activitys = db.query(Activity).all()
    return activitys

def update_activity(activity_id: int, updated_activity: ActivityUpdate, db: db_dependency):
    db_activity = db.query(Activity).filter(activity_id == Activity.activityId).first()

    if db_activity is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_activity.model_dump().items():
        setattr(db_activity, key, value)
    
    db.commit()
    return db_activity

def delete_activity(activity_id: int, activity_soft_delete: ActivityDelete, db: db_dependency):
    db_activity = db.query(Activity).filter(Activity.activityId == activity_id).first()

    for key, value in activity_soft_delete.model_dump().items():
        setattr(db_activity, key, value)

    db.commit()
    return {"message":"Activity Record Deleted Successfully."}