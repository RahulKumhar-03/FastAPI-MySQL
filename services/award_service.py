from repository import award_repo as award_repo
from database import db_dependency
from schema.award import AwardCreate, AwardUpdate

def get_award(db: db_dependency):
    return award_repo.get_awards(db)

def create_award(new_award: AwardCreate, db: db_dependency):
    return award_repo.create_award(new_award, db)

def update_award(award_id: int, updated_award: AwardUpdate, db: db_dependency):
    return award_repo.update_award(award_id, updated_award, db)

def delete_award(award_id: int, db: db_dependency):
    return award_repo.delete_award(award_id, db)