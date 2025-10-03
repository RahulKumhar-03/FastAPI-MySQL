from repository import personal_info_repo as PersonalInfoRepo
from database import db_dependency
from schema.personalInfo import PersonalInfoCreate, PersonalInfoUpdate

def getPersonalInfos(db: db_dependency):
    return PersonalInfoRepo.get_personal_infos(db)

def createPersonalInfo(new_personal_info: PersonalInfoCreate, db: db_dependency):
    return PersonalInfoRepo.create_personal_info(new_personal_info, db)

def updatePersonalInfo(peronsalInfoId: int, updated_personal_info: PersonalInfoUpdate, db: db_dependency):
    return PersonalInfoRepo.update_personal_info(peronsalInfoId, updated_personal_info, db)

def deletePersonalInfo(personalInfoId: int, db: db_dependency):
    return PersonalInfoRepo.delete_personal_info(personalInfoId, db)