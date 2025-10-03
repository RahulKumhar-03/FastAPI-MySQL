from schema.internship import Internship, InternshipCreate, InternshipUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_internship(new_internship: InternshipCreate, db: db_dependency):
    db_internship = Internship(**new_internship.dict())
    db.add(db_internship)
    db.commit()
    return db_internship

def get_internships(db: db_dependency):
    internships = db.query(Internship).all()
    return internships

def update_internship(internship_id: int, updated_internship: InternshipUpdate, db: db_dependency):
    db_internship = db.query(Internship).filter(internship_id == Internship.internshipId).first()

    if db_internship is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_internship.dict(exclude_unset=True).items():
        setattr(db_internship, key, value)
    
    db.commit()
    return db_internship

def delete_internship(internship_id: int, db: db_dependency):
    db_internship = db.query(Internship).filter(Internship.internshipId == internship_id).first()

    db.delete(db_internship)
    db.commit()
    return {"message":"Internship Record Deleted Successfully."}