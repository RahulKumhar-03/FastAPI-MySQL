from repository import honor_repo as honor_repo
from database import db_dependency
from schema.honor import HonorCreate, HonorUpdate

def get_honor(db: db_dependency):
    return honor_repo.get_honors(db)

def create_honor(new_honor: HonorCreate, db: db_dependency):
    return honor_repo.create_honor(new_honor, db)

def update_honor(honor_id: int, updated_honor: HonorUpdate, db: db_dependency):
    return honor_repo.update_honor(honor_id, updated_honor, db)

def delete_honor(honor_id: int, db: db_dependency):
    return honor_repo.delete_honor(honor_id, db)