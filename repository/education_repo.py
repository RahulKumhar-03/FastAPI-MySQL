from database import db_dependency
from schema.education import EducationCreate, Education

def createEducation(new_education: EducationCreate, db: db_dependency):
    db_education = Education(**new_education.dict())
    db.add(db_education)
    db.commit()

def getEducation(db: db_dependency):
    educations = db.query(Education).all()
    return educations

def deleteEducation(educationId: int, db: db_dependency):
    db_education = db.query(Education).filter(Education.educationId == educationId).first()

    db.delete(db_education)
    db.commit()
    return {"message":"Education Record Deleted Successfully."}
