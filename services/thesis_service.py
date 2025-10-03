from repository import thesis_repo as thesisRepo
from database import db_dependency
from schema.thesis import ThesisCreate, ThesisUpdate

def getThesis(db: db_dependency):
    return thesisRepo.get_thesis(db)

def createThesis(new_thesis: ThesisCreate, db: db_dependency):
    return thesisRepo.create_thesis(new_thesis, db)

def updateThesis(thesisId: int, updated_thesis: ThesisUpdate, db: db_dependency):
    return thesisRepo.update_thesis(thesisId, updated_thesis, db)

def deleteThesis(thesisId: int, db: db_dependency):
    return thesisRepo.deleteThesis(thesisId, db)