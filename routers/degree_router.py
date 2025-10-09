from fastapi import APIRouter
from database import db_dependency
from services import degree_service as DegreeService
from schema.degree import DegreeCreate, DegreeBase, DegreeResponse, DegreeDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[DegreeResponse])
def getDegrees(db: db_dependency, user: user_dependency):
    return DegreeService.getDegrees(db)

@router.post("/")
def createDegree(new_degree: DegreeCreate, db: db_dependency, user: user_dependency):
    return DegreeService.createDegree(new_degree, db, user)

@router.put("/{degreeId}")
def updateDegree(degreeId: int, updated_degree: DegreeBase, db: db_dependency, user: user_dependency):
    return DegreeService.updateDegree(degreeId, updated_degree, db, user)

@router.delete("/{degreeId}")
def deleteDegree(degreeId: int, degree_delete: DegreeDelete, db: db_dependency, user: user_dependency):
    return DegreeService.deleteDegree(degreeId, degree_delete, db, user)