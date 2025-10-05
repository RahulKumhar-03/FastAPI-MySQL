from repository import awardMapping_repo as awardMapping_repo
from database import db_dependency
from schema.awardMapping import awardMappingCreate, AwardMappingUpdate

def get_awardMapping(db: db_dependency):
    return awardMapping_repo.get_awardMapping(db)

def create_awardMapping(new_awardMapping: awardMappingCreate, db: db_dependency):
    return awardMapping_repo.create_awardMapping(new_awardMapping, db)

def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingUpdate, db: db_dependency):
    return awardMapping_repo.update_awardMapping(awardMapping_id, updated_awardMapping, db)

def delete_awardMapping(awardMapping_id: int, db: db_dependency):
    return awardMapping_repo.delete_awardMapping(awardMapping_id, db)