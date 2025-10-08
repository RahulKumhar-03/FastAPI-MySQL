from schema.internship import Internship, InternshipCreate, InternshipUpdate, InternshipDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_internship(new_internship: InternshipCreate, db: db_dependency):
    db_internship = Internship(**new_internship.model_dump())
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

    for key, value in updated_internship.model_dump().items():
        setattr(db_internship, key, value)
    
    db.commit()
    return db_internship

def delete_internship(internship_id: int, internship_delete: InternshipDelete, db: db_dependency):
    db_internship = db.query(Internship).filter(Internship.internshipId == internship_id).first()

    for key, value in internship_delete.model_dump().items():
        setattr(db_internship, key, value)
        
    db.commit()
    return {"message":"Internship Record Deleted Successfully."}