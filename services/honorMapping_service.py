from repository import honorMapping_repo as honorMapping_repo
from database import db_dependency
from schema.honorMapping import HonorMappingBase, HonorMappingDelete

def get_honorMapping(db: db_dependency):
    return honorMapping_repo.get_honorMapping(db)

def create_honorMapping(new_honorMapping: HonorMappingBase, db: db_dependency, currentUser):
    return honorMapping_repo.create_honorMapping(new_honorMapping, db, currentUser)

def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingBase, db: db_dependency, currentUser):
    return honorMapping_repo.update_honorMapping(honorMapping_id, updated_honorMapping, db, currentUser)

def delete_honorMapping(honorMapping_id: int, honorMapping_delete: HonorMappingDelete, db: db_dependency, currentUser):
    return honorMapping_repo.delete_honorMapping(honorMapping_id, honorMapping_delete, db, currentUser)