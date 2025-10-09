from fastapi import APIRouter
from database import db_dependency
from services import honor_service as honorService
from schema.honor import HonorBase, HonorResponse, HonorDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[HonorResponse])
def get_honor(db: db_dependency, user: user_dependency):
    return honorService.get_honor(db)

@router.post("/")
def create_honor(new_honor: HonorBase, db: db_dependency, user: user_dependency):
    return honorService.create_honor(new_honor, db, user)

@router.put("/{honor_id}")
def update_honor(honor_id: int, updated_honor: HonorBase, db: db_dependency, user: user_dependency):
    return honorService.update_honor(honor_id, updated_honor, db, user)

@router.delete("/{honor_id}")
def delete_honor(honor_id: int, honor_delete: HonorDelete, db: db_dependency, user: user_dependency):
    return honorService.delete_honor(honor_id, honor_delete, db, user)