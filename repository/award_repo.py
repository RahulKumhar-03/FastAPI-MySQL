from schema.award import Award, AwardCreate, AwardUpdate, AwardDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_award(new_award: AwardCreate, db: db_dependency):
    db_award = Award(**new_award.model_dump())
    db.add(db_award)
    db.commit()
    return db_award

def get_awards(db: db_dependency):
    awards = db.query(Award).all()
    return awards

def update_award(award_id: int, updated_award: AwardUpdate, db: db_dependency):
    db_award = db.query(Award).filter(award_id == Award.awardId).first()

    if db_award is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_award.dict(exclude_unset=True).items():
        setattr(db_award, key, value)
    
    db.commit()
    return db_award

def delete_award(award_id: int, award_delete: AwardDelete, db: db_dependency):
    db_award = db.query(Award).filter(Award.awardId == award_id).first()

    for key, value in award_delete.dict(exclude_unset=True).items():
        setattr(db_award, key, value)

    db.commit()
    return {"message":"Award Record Deleted Successfully."}