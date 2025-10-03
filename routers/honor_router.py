from fastapi import APIRouter
from database import db_dependency
from services import honor_service as honorService
from schema.honor import HonorCreate, HonorUpdate

router = APIRouter()

@router.get("/")
def get_honor(db: db_dependency):
    return honorService.get_honor(db)

@router.post("/")
def create_honor(new_honor: HonorCreate, db: db_dependency):
    return honorService.create_honor(new_honor, db)

@router.put("/{honor_id}")
def update_honor(honor_id: int, updated_honor: HonorUpdate, db: db_dependency):
    return honorService.update_honor(honor_id, updated_honor, db)

@router.delete("/{honor_id}")
def delete_honor(honor_id: int, db: db_dependency):
    return honorService.delete_honor(honor_id, db)