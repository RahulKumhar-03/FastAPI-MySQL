from schema.thesis import Thesis, ThesisCreate, ThesisUpdate, ThesisResponse
from database import db_dependency
from fastapi import HTTPException, status


def create_thesis(new_thesis: ThesisCreate, db: db_dependency):
    db_thesis = Thesis(**new_thesis.dict())
    db.add(db_thesis)
    db.commit()
    return db_thesis

def get_thesis(db: db_dependency) -> list[ThesisResponse]:
    thesis = db.query(Thesis).all()
    return thesis

def update_thesis(thesis_id: int, updated_thesis: ThesisUpdate, db: db_dependency):
    db_thesis = db.query(Thesis).filter(thesis_id == Thesis.thesisId).first()

    if db_thesis is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_thesis.dict(exclude_unset=True).items():
        setattr(db_thesis, key, value)
    
    db.commit()
    return db_thesis

def delete_thesis(thesis_id: int, db: db_dependency):
    db_thesis = db.query(Thesis).filter(Thesis.thesisId == thesis_id).first()

    db.delete(db_thesis)
    db.commit()
    return {"message":"Online Course Record Deleted Successfully."}