from schema.award import Award, AwardBase, AwardDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_award(new_award: AwardBase, db: db_dependency, currentUser):
    db_award = Award(
        **new_award.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_award)
    db.commit()
    return db_award

def get_awards(db: db_dependency):
    awards = db.query(Award).all()
    return awards

def update_award(award_id: int, updated_award: AwardBase, db: db_dependency, currentUser):
    db_award = db.query(Award).filter(award_id == Award.awardId).first()

    if db_award is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_award.model_dump().items():
        setattr(db_award, key, value)

    db_award.changedBy = currentUser["userId"]
    
    db.commit()
    return db_award

def delete_award(award_id: int, award_delete: AwardDelete, db: db_dependency, currentUser):
    db_award = db.query(Award).filter(Award.awardId == award_id).first()

    for key, value in award_delete.model_dump().items():
        setattr(db_award, key, value)

    db_award.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"Award Record Deleted Successfully."}