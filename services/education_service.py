from repository import education_repo as EducationRepo
from database import db_dependency
from schema.education import EducationCreate

def getEducation(db: db_dependency):
    return EducationRepo.getEducation(db)

def createEducation(new_education: EducationCreate, db: db_dependency):
    return EducationRepo.createEducation(new_education, db)

def deleteEducation(educationId: int, db: db_dependency):
    return EducationRepo.deleteEducation(educationId, db)