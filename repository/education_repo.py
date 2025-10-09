from database import db_dependency
from schema.education import EducationBase, Education, EducationDelete

def createEducation(new_education: EducationBase, db: db_dependency, currentUser):
    db_education = Education(
        **new_education.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_education)
    db.commit()

def getEducation(db: db_dependency):
    educations = db.query(Education).all()
    return educations

def deleteEducation(educationId: int, education_delete: EducationDelete, db: db_dependency, currentUser):
    db_education = db.query(Education).filter(Education.educationId == educationId).first()

    for key, value in education_delete.model_dump().items():
        setattr(db_education, key, value)

    db_education.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"Education Record Deleted Successfully."}
