from repository import thesis_repo as thesisRepo
from database import db_dependency
from schema.thesis import ThesisCreate, ThesisBase, ThesisDelete

def getThesis(db: db_dependency):
    return thesisRepo.get_thesis(db)

def createThesis(new_thesis: ThesisCreate, db: db_dependency, currentUser):
    return thesisRepo.create_thesis(new_thesis, db, currentUser)

def updateThesis(thesisId: int, updated_thesis: ThesisBase, db: db_dependency, currentUser):
    return thesisRepo.update_thesis(thesisId, updated_thesis, db, currentUser)

def deleteThesis(thesisId: int, thesis_delete: ThesisDelete, db: db_dependency, currentUser):
    return thesisRepo.deleteThesis(thesisId, thesis_delete, db, currentUser)