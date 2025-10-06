from fastapi import APIRouter
from database import db_dependency
from services import thesis_service as thesisService
from schema.thesis import ThesisCreate, ThesisUpdate, ThesisResponse, ThesisDelete

router = APIRouter()

@router.get("/", response_model=list[ThesisResponse])
def getThesis(db: db_dependency):
    return thesisService.getThesis(db)

@router.post("/")
def createThesis(new_thesis: ThesisCreate, db: db_dependency):
    return thesisService.createThesis(new_thesis, db)

@router.put("/{thesisId}")
def updateThesis(thesisId: int, updated_thesis: ThesisUpdate, db: db_dependency):
    return thesisService.updateThesis(thesisId, updated_thesis, db)

@router.delete("/{thesisId}")
def deleteThesis(thesisId: int, thesis_delete: ThesisDelete, db: db_dependency):
    return thesisService.deleteThesis(thesisId, thesis_delete, db)