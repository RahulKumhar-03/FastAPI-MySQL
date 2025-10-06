from schema.degree import Degree, DegreeCreate, DegreeUpdate, DegreeDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_degree(new_degree: DegreeCreate, db: db_dependency):
    db_degree = Degree(**new_degree.dict())
    db.add(db_degree)
    db.commit()
    return db_degree

def get_degrees(db: db_dependency):
    degrees = db.query(Degree).all()
    return degrees

def update_degree(degree_id: int, updated_degree: DegreeUpdate, db: db_dependency):
    db_degree = db.query(Degree).filter(degree_id == Degree.degreeId).first()

    if db_degree is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_degree.dict(exclude_unset=True).items():
        setattr(db_degree, key, value)
    
    db.commit()
    return db_degree

def delete_degree(degreeId: int, degree_delete: DegreeDelete, db: db_dependency):
    db_degree = db.query(Degree).filter(Degree.degreeId == degreeId).first()

    for key, value in degree_delete.dict(exclude_unset=True).items():
        setattr(db_degree, key, value)
        
    db.commit()
    return {"message":"Degree Record Deleted Successfully."}