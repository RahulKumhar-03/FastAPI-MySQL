from repository import activityMapping_repo as activityMapping_repo
from database import db_dependency
from schema.activityMapping import ActivityMappingCreate, ActivityMappingUpdate

def get_activityMapping(db: db_dependency):
    return activityMapping_repo.get_activityMapping(db)

def create_activityMapping(new_activityMapping: ActivityMappingCreate, db: db_dependency):
    return activityMapping_repo.create_activityMapping(new_activityMapping, db)

def update_activityMapping(activityMapping_id: int, updated_activityMapping: ActivityMappingUpdate, db: db_dependency):
    return activityMapping_repo.update_activityMapping(activityMapping_id, updated_activityMapping, db)

def delete_activityMapping(activityMapping_id: int, db: db_dependency):
    return activityMapping_repo.delete_activityMapping(activityMapping_id, db)