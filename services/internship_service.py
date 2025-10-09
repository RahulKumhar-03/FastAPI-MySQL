from repository import internship_repo as internshipRepo
from database import db_dependency
from schema.internship import InternshipCreate, InternshipBase, InternshipDelete

def get_internship(db: db_dependency):
    return internshipRepo.get_internships(db)

def create_internship(new_internship: InternshipCreate, db: db_dependency, currentUser):
    return internshipRepo.create_internship(new_internship, db, currentUser)

def update_internship(internshipId: int, updated_internship: InternshipBase, db: db_dependency, currentUser):
    return internshipRepo.update_internship(internshipId, updated_internship, db, currentUser)

def delete_internship(internshipId: int, internship_delete: InternshipDelete, db: db_dependency, currentUser):
    return internshipRepo.delete_internship(internshipId, internship_delete, db, currentUser)