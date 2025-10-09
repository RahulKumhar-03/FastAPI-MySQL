from schema.internship import Internship, InternshipCreate, InternshipBase, InternshipDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_internship(new_internship: InternshipCreate, db: db_dependency, currentUser):
    db_internship = Internship(**new_internship.model_dump(), createdBy = currentUser["userId"])
    db.add(db_internship)
    db.commit()
    return db_internship

def get_internships(db: db_dependency):
    internships = db.query(Internship).all()
    return internships

def update_internship(internship_id: int, updated_internship: InternshipBase, db: db_dependency, currentUser):
    db_internship = db.query(Internship).filter(internship_id == Internship.internshipId).first()

    if db_internship is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_internship.model_dump().items():
        setattr(db_internship, key, value)

    db_internship.changedBy = currentUser["userId"]
    
    db.commit()
    return db_internship

def delete_internship(internship_id: int, internship_delete: InternshipDelete, db: db_dependency, currentUser):
    db_internship = db.query(Internship).filter(Internship.internshipId == internship_id).first()

    for key, value in internship_delete.model_dump().items():
        setattr(db_internship, key, value)

    db_internship.deletedBy = currentUser["userId"]
        
    db.commit()
    return {"message":"Internship Record Deleted Successfully."}