from fastapi import APIRouter
from database import db_dependency
from services import thesis_service as thesisService
from schema.thesis import ThesisCreate, ThesisBase, ThesisResponse, ThesisDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[ThesisResponse])
def getThesis(db: db_dependency, user: user_dependency):
    return thesisService.getThesis(db)

@router.post("/")
def createThesis(new_thesis: ThesisCreate, db: db_dependency, user: user_dependency):
    return thesisService.createThesis(new_thesis, db, user)

@router.put("/{thesisId}")
def updateThesis(thesisId: int, updated_thesis: ThesisBase, db: db_dependency, user: user_dependency):
    return thesisService.updateThesis(thesisId, updated_thesis, db, user)

@router.delete("/{thesisId}")
def deleteThesis(thesisId: int, thesis_delete: ThesisDelete, db: db_dependency, user: user_dependency):
    return thesisService.deleteThesis(thesisId, thesis_delete, db, user)