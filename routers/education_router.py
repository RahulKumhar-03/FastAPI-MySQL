from fastapi import APIRouter
from database import db_dependency
from services import education_service as EducationService
from schema.education import EducationCreate

router = APIRouter()

@router.get("/")
def getEducations(db: db_dependency):
    return EducationService.getEducation(db)

@router.post("/")
def createEducation(new_education: EducationCreate, db: db_dependency):
    return EducationService.createEducation(new_education, db)


@router.delete("/{educationId}")
def deleteEducation(educationId: int, db: db_dependency):
    return EducationService.deleteEducation(educationId, db)

