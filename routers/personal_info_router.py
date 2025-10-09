from fastapi import APIRouter
from database import db_dependency
from services import personal_info_service as PersonalInfoService
from schema.personalInfo import PersonalInfoCreate, PersonalInfoBase, PersonalInfoResponse, PersonalInfoDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[PersonalInfoResponse])
def getPersonalInfos(db: db_dependency, user: user_dependency):
    return PersonalInfoService.getPersonalInfos(db)

@router.post("/")
def createPersonalInfo(new_personal_info: PersonalInfoCreate, db: db_dependency, user: user_dependency):
    return PersonalInfoService.createPersonalInfo(new_personal_info, db, user)

@router.put("/{peronsalInfoId}")
def updatePersonalInfo(personalInfoId: int, updated_personal_info: PersonalInfoBase, db: db_dependency, user: user_dependency):
    return PersonalInfoService.updatePersonalInfo(personalInfoId, updated_personal_info, db, user)

@router.delete("/{personalInfoId}")
def deletePersonalInfo(personalInfoId: int, personalInfo_delete: PersonalInfoDelete, db: db_dependency, user: user_dependency):
    return PersonalInfoService.deletePersonalInfo(personalInfoId, personalInfo_delete, db, user)