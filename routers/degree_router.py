from fastapi import APIRouter
from database import db_dependency
from services import degree_service as DegreeService
from schema.degree import DegreeCreate, DegreeUpdate

router = APIRouter()

@router.get("/")
def getDegrees(db: db_dependency):
    return DegreeService.getDegrees(db)

@router.post("/")
def createDegree(new_degree: DegreeCreate, db: db_dependency):
    return DegreeService.createDegree(new_degree, db)

@router.put("/{degreeId}")
def updateDegree(degreeId: int, updated_degree: DegreeUpdate, db: db_dependency):
    return DegreeService.updateDegree(degreeId, updated_degree, db)

@router.delete("/{degreeId}")
def deleteDegree(degreeId: int, db: db_dependency):
    return DegreeService.deleteDegree(degreeId, db)