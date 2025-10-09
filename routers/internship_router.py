from fastapi import APIRouter
from database import db_dependency
from services import internship_service as internshipService
from schema.internship import InternshipCreate, InternshipBase, InternshipResponse, InternshipDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[InternshipResponse])
def get_internship(db: db_dependency, user: user_dependency):
    return internshipService.get_internship(db)

@router.post("/")
def create_internship(new_internship: InternshipCreate, db: db_dependency, user: user_dependency):
    return internshipService.create_internship(new_internship, db, user)

@router.put("/{internshipId}")
def update_internship(internshipId: int, updated_internship: InternshipBase, db: db_dependency, user: user_dependency):
    return internshipService.update_internship(internshipId, updated_internship, db, user)

@router.delete("/{internshipId}")
def delete_internship(internshipId: int, internship_delete: InternshipDelete, db: db_dependency, user: user_dependency):
    return internshipService.delete_internship(internshipId, internship_delete, db, user)