from repository import skillValidatedMapping_repo as skillValidatedMappingRepo
from database import db_dependency
from schema.skillValidatedMapping import SkillValidatedMappingCreate, SkillValidatedMappingUpdate

def get_skillValidatedMapping(db: db_dependency):
    return skillValidatedMappingRepo.get_skillValidatedMapping(db)

def create_skillValidatedMapping(new_skillValidatedMapping: SkillValidatedMappingCreate, db: db_dependency):
    return skillValidatedMappingRepo.create_skillValidatedMapping(new_skillValidatedMapping, db)

def update_skillValidatedMapping(skillValidatedMapping_id: int, updated_skillValidatedMapping: SkillValidatedMappingUpdate, db: db_dependency):
    return skillValidatedMappingRepo.update_skillValidatedMapping(skillValidatedMapping_id, updated_skillValidatedMapping, db)

def delete_skillValidatedMapping(skillValidatedMapping_id: int, db: db_dependency):
    return skillValidatedMappingRepo.delete_skillValidatedMapping(skillValidatedMapping_id, db)