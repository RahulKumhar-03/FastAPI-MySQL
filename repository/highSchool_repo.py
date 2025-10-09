from schema.highSchool import HighSchool, HighSchoolCreate, HighSchoolBase, HighSchoolDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_highSchool(new_highSchool: HighSchoolCreate, db: db_dependency, currentUser):
    db_highSchool = HighSchool(
        **new_highSchool.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_highSchool)
    db.commit()
    return db_highSchool

def get_highSchools(db: db_dependency):
    highSchools = db.query(HighSchool).all()
    return highSchools

def update_highSchool(highSchoolId: int, updated_highSchool: HighSchoolBase, db: db_dependency, currentUser):
    db_highSchool = db.query(HighSchool).filter(highSchoolId == HighSchool.highSchoolId).first()

    if db_highSchool is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_highSchool.model_dump().items():
        setattr(db_highSchool, key, value)

    db_highSchool.changedBy = currentUser["userId"]
    
    db.commit()
    return db_highSchool

def delete_highSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency, currentUser):
    db_highSchool = db.query(HighSchool).filter(HighSchool.highSchoolId == highSchoolId).first()

    for key, value in highSchool_delete.model_dump().items():
        setattr(db_highSchool, key, value)

    db_highSchool.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"High School Record Deleted Successfully."}