from database import db_dependency
from schema.education import EducationCreate, Education, EducationDelete

def createEducation(new_education: EducationCreate, db: db_dependency):
    db_education = Education(**new_education.dict())
    db.add(db_education)
    db.commit()

def getEducation(db: db_dependency):
    educations = db.query(Education).all()
    return educations

def deleteEducation(educationId: int, education_delete: EducationDelete, db: db_dependency):
    db_education = db.query(Education).filter(Education.educationId == educationId).first()

    for key, value in education_delete.dict(exclude_unset=True).items():
        setattr(db_education, key, value)

    db.commit()
    return {"message":"Education Record Deleted Successfully."}
