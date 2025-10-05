from repository import honorMapping_repo as honorMapping_repo
from database import db_dependency
from schema.honorMapping import HonorMappingCreate, HonorMappingUpdate

def get_honorMapping(db: db_dependency):
    return honorMapping_repo.get_honorMapping(db)

def create_honorMapping(new_honorMapping: HonorMappingCreate, db: db_dependency):
    return honorMapping_repo.create_honorMapping(new_honorMapping, db)

def update_honorMapping(honorMapping_id: int, updated_honorMapping: HonorMappingUpdate, db: db_dependency):
    return honorMapping_repo.update_honorMapping(honorMapping_id, updated_honorMapping, db)

def delete_honorMapping(honorMapping_id: int, db: db_dependency):
    return honorMapping_repo.delete_honorMapping(honorMapping_id, db)