from repository import degree_repo as DegreeRepo
from database import db_dependency
from schema.degree import DegreeCreate, DegreeUpdate, DegreeDelete

def getDegrees(db: db_dependency):
    return DegreeRepo.get_degrees(db)

def createDegree(new_degree: DegreeCreate, db: db_dependency):
    return DegreeRepo.create_degree(new_degree, db)

def updateDegree(degreeId: int, updated_degree: DegreeUpdate, db: db_dependency):
    return DegreeRepo.update_degree(degreeId, updated_degree, db)

def deleteDegree(degreeId: int, degree_delete: DegreeDelete, db: db_dependency):
    return DegreeRepo.delete_degree(degreeId, degree_delete, db)