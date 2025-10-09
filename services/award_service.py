from repository import award_repo as award_repo
from database import db_dependency
from schema.award import AwardBase, AwardDelete

def get_award(db: db_dependency):
    return award_repo.get_awards(db)

def create_award(new_award: AwardBase, db: db_dependency, currentUser):
    return award_repo.create_award(new_award, db, currentUser)

def update_award(award_id: int, updated_award: AwardBase, db: db_dependency, currentUser):
    return award_repo.update_award(award_id, updated_award, db, currentUser)

def delete_award(award_id: int, award_delete: AwardDelete, db: db_dependency, currentUser):
    return award_repo.delete_award(award_id, award_delete, db, currentUser)