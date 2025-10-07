from repository import highSchool_repo as highSchoolRepo
from database import db_dependency
from schema.highSchool import HighSchoolCreate, HighSchoolUpdate, HighSchoolDelete

def getHighSchools(db: db_dependency):
    return highSchoolRepo.get_highSchools(db)

def createHighSchool(new_highSchool: HighSchoolCreate, db: db_dependency):
    return highSchoolRepo.create_highSchool(new_highSchool, db)

def updateHighSchool(highSchoolId: int, updated_highSchool: HighSchoolUpdate, db: db_dependency):
    return highSchoolRepo.update_highSchool(highSchoolId, updated_highSchool, db)

def deleteHighSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency):
    return highSchoolRepo.deleteHighSchool(highSchoolId, highSchool_delete, db)