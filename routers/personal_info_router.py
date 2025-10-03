from fastapi import APIRouter
from database import db_dependency
from services import personal_info_service as PersonalInfoService
from schema.personalInfo import PersonalInfoCreate, PersonalInfoUpdate

router = APIRouter()

@router.get("/")
def getPersonalInfos(db: db_dependency):
    return PersonalInfoService.getPersonalInfos(db)

@router.post("/")
def createPersonalInfo(new_personal_info: PersonalInfoCreate, db: db_dependency):
    return PersonalInfoService.createPersonalInfo(new_personal_info, db)

@router.put("/{peronsalInfoId}")
def updatePersonalInfo(personalInfoId: int, updated_personal_info: PersonalInfoUpdate, db: db_dependency):
    return PersonalInfoService.updatePersonalInfo(personalInfoId, updated_personal_info, db)

@router.delete("/{personalInfoId}")
def deletePersonalInfo(personalInfoId: int, db: db_dependency):
    return PersonalInfoService.deletePersonalInfo(personalInfoId, db)