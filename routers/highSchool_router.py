from fastapi import APIRouter
from database import db_dependency
from services import highSchool_service as highSchoolService
from schema.highSchool import HighSchoolCreate,HighSchoolUpdate, HighSchoolResponse, HighSchoolDelete

router = APIRouter()

@router.get("/", response_model=list[HighSchoolResponse])
def getHighSchools(db: db_dependency):
    return highSchoolService.getHighSchools(db)

@router.post("/")
def createhighSchool(new_highSchool: HighSchoolCreate, db: db_dependency):
    return highSchoolService.createHighSchool(new_highSchool, db)

@router.put("/{highSchoolId}")
def updateHighSchool(highSchoolId: int, updated_highSchool: HighSchoolUpdate, db: db_dependency):
    return highSchoolService.updateHighSchool(highSchoolId, updated_highSchool, db)

@router.delete("/{highSchoolId}")
def deleteHighSchool(highSchoolId: int, highSchool_delete: HighSchoolDelete, db: db_dependency):
    return highSchoolService.deleteHighSchool(highSchoolId, highSchool_delete, db)