from fastapi import APIRouter
from database import db_dependency
from services import education_service as EducationService
from schema.education import EducationCreate, EducationResponse, EducationDelete

router = APIRouter()

@router.get("/", response_model=list[EducationResponse])
def getEducations(db: db_dependency):
    return EducationService.getEducation(db)

@router.post("/")
def createEducation(new_education: EducationCreate, db: db_dependency):
    return EducationService.createEducation(new_education, db)


@router.delete("/{educationId}")
def deleteEducation(educationId: int, education_delete: EducationDelete, db: db_dependency):
    return EducationService.deleteEducation(educationId, education_delete, db)

