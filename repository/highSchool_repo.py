from schema.highSchool import HighSchool, HighSchoolCreate, HighSchoolUpdate, HighSchoolDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_highSchool(new_highSchool: HighSchoolCreate, db: db_dependency):
    db_highSchool = HighSchool(**new_highSchool.dict())
    db.add(db_highSchool)
    db.commit()
    return db_highSchool

def get_highSchools(db: db_dependency):
    highSchools = db.query(HighSchool).all()
    return highSchools

def update_highSchool(highSchoolId: int, updated_highSchool: HighSchoolUpdate, db: db_dependency):
    db_highSchool = db.query(HighSchool).filter(highSchoolId == HighSchool.highSchoolId).first()

    if db_highSchool is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_highSchool.dict(exclude_unset=True).items():
        setattr(db_highSchool, key, value)
    
    db.commit()
    return db_highSchool

def delete_highSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency):
    db_highSchool = db.query(HighSchool).filter(HighSchool.highSchoolId == highSchoolId).first()

    for key, value in highSchool_delete.dict(exclude_unset=True).items():
        setattr(db_highSchool, key, value)

    db.commit()
    return {"message":"High School Record Deleted Successfully."}