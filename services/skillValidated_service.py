from repository import skillValidated_repo as skillValidated_repo
from database import db_dependency
from schema.skillValidated import SkillValidatedCreate, SkillValidatedUpdate, SkillValidatedDelete

def get_skillValidated(db: db_dependency):
    return skillValidated_repo.get_skillValidated(db)

def create_skillValidated(new_skillValidated: SkillValidatedCreate, db: db_dependency):
    return skillValidated_repo.create_skillValidated(new_skillValidated, db)

def update_skillValidated(skillValidated_id: int, updated_skillValidated: SkillValidatedUpdate, db: db_dependency):
    return skillValidated_repo.update_skillValidated(skillValidated_id, updated_skillValidated, db)

def delete_skillValidated(skillValidated_id: int, skillValidated_delete: SkillValidatedDelete, db: db_dependency):
    return skillValidated_repo.delete_skillValidated(skillValidated_id, skillValidated_delete, db)