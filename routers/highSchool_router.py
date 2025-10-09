from fastapi import APIRouter
from database import db_dependency
from services import highSchool_service as highSchoolService
from schema.highSchool import HighSchoolCreate, HighSchoolBase, HighSchoolResponse, HighSchoolDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[HighSchoolResponse])
def getHighSchools(db: db_dependency, user: user_dependency):
    return highSchoolService.getHighSchools(db)

@router.post("/")
def createhighSchool(new_highSchool: HighSchoolCreate, db: db_dependency, user: user_dependency):
    return highSchoolService.createHighSchool(new_highSchool, db, user)

@router.put("/{highSchoolId}")
def updateHighSchool(highSchoolId: int, updated_highSchool: HighSchoolBase, db: db_dependency, user: user_dependency):
    return highSchoolService.updateHighSchool(highSchoolId, updated_highSchool, db, user)

@router.delete("/{highSchoolId}")
def deleteHighSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency, user: user_dependency):
    return highSchoolService.deleteHighSchool(highSchoolId, highSchool_delete, db, user)