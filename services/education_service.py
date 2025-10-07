from repository import education_repo as EducationRepo
from database import db_dependency
from schema.education import EducationCreate, EducationDelete

def getEducation(db: db_dependency):
    return EducationRepo.getEducation(db)

def createEducation(new_education: EducationCreate, db: db_dependency):
    return EducationRepo.createEducation(new_education, db)

def deleteEducation(educationId: int, education_delete: EducationDelete, db: db_dependency):
    return EducationRepo.deleteEducation(educationId, education_delete, db)