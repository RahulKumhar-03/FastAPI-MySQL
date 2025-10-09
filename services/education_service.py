from repository import education_repo as EducationRepo
from database import db_dependency
from schema.education import EducationBase, EducationDelete

def getEducation(db: db_dependency):
    return EducationRepo.getEducation(db)

def createEducation(new_education: EducationBase, db: db_dependency, currentUser):
    return EducationRepo.createEducation(new_education, db, currentUser)

def deleteEducation(educationId: int, education_delete: EducationDelete, db: db_dependency, currentUser):
    return EducationRepo.deleteEducation(educationId, education_delete, db, currentUser)