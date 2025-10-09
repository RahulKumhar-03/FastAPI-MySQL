from repository import degree_repo as DegreeRepo
from database import db_dependency
from schema.degree import DegreeCreate, DegreeBase, DegreeDelete

def getDegrees(db: db_dependency):
    return DegreeRepo.get_degrees(db)

def createDegree(new_degree: DegreeCreate, db: db_dependency, currentUser):
    return DegreeRepo.create_degree(new_degree, db, currentUser)

def updateDegree(degreeId: int, updated_degree: DegreeBase, db: db_dependency, currentUser):
    return DegreeRepo.update_degree(degreeId, updated_degree, db, currentUser)

def deleteDegree(degreeId: int, degree_delete: DegreeDelete, db: db_dependency, currentUser):
    return DegreeRepo.delete_degree(degreeId, degree_delete, db, currentUser)