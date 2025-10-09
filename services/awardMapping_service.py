from repository import awardMapping_repo as awardMapping_repo
from database import db_dependency
from schema.awardMapping import AwardMappingBase, AwardMappingDelete

def get_awardMapping(db: db_dependency):
    return awardMapping_repo.get_awardMapping(db)

def create_awardMapping(new_awardMapping: AwardMappingBase, db: db_dependency, currentUser):
    return awardMapping_repo.create_awardMapping(new_awardMapping, db, currentUser)

def update_awardMapping(awardMapping_id: int, updated_awardMapping: AwardMappingBase, db: db_dependency, currentUser):
    return awardMapping_repo.update_awardMapping(awardMapping_id, updated_awardMapping, db, currentUser)

def delete_awardMapping(awardMapping_id: int, awardMapping_delete: AwardMappingDelete, db: db_dependency, currentUser):
    return awardMapping_repo.delete_awardMapping(awardMapping_id, awardMapping_delete, db, currentUser)