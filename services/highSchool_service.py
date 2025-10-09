from repository import highSchool_repo as highSchoolRepo
from database import db_dependency
from schema.highSchool import HighSchoolCreate, HighSchoolBase, HighSchoolDelete

def getHighSchools(db: db_dependency):
    return highSchoolRepo.get_highSchools(db)

def createHighSchool(new_highSchool: HighSchoolCreate, db: db_dependency, currentUser):
    return highSchoolRepo.create_highSchool(new_highSchool, db, currentUser)

def updateHighSchool(highSchoolId: int, updated_highSchool: HighSchoolBase, db: db_dependency, currentUser):
    return highSchoolRepo.update_highSchool(highSchoolId, updated_highSchool, db, currentUser)

def deleteHighSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency, currentUser):
    return highSchoolRepo.deleteHighSchool(highSchoolId, highSchool_delete, db, currentUser)