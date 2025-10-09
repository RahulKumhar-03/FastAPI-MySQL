from repository import skillValidatedMapping_repo as skillValidatedMappingRepo
from database import db_dependency
from schema.skillValidatedMapping import SkillValidatedMappingBase, SkillValidatedMappingDelete

def get_skillValidatedMapping(db: db_dependency):
    return skillValidatedMappingRepo.get_skillValidatedMapping(db)

def create_skillValidatedMapping(new_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, currentUser):
    return skillValidatedMappingRepo.create_skillValidatedMapping(new_skillValidatedMapping, db, currentUser)

def update_skillValidatedMapping(skillValidatedMapping_id: int, updated_skillValidatedMapping: SkillValidatedMappingBase, db: db_dependency, currentUser):
    return skillValidatedMappingRepo.update_skillValidatedMapping(skillValidatedMapping_id, updated_skillValidatedMapping, db, currentUser)

def delete_skillValidatedMapping(skillValidatedMapping_id: int, skillValidatedMapping_delete: SkillValidatedMappingDelete, db: db_dependency, currentUser):
    return skillValidatedMappingRepo.delete_skillValidatedMapping(skillValidatedMapping_id, skillValidatedMapping_delete, db, currentUser)