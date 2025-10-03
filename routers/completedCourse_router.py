from fastapi import APIRouter
from database import db_dependency
from services import completedCourse_service as completedCourseService
from schema.completedCourse import CompletedCourseCreate, CompletedCourseUpdate

router = APIRouter()

@router.get("/")
def get_completedCourse(db: db_dependency):
    return completedCourseService.get_completedCourse(db)

@router.post("/")
def create_completedCourse(new_completedCourse: CompletedCourseCreate, db: db_dependency):
    return completedCourseService.create_completedCourse(new_completedCourse, db)

@router.put("/{completedCourseId}")
def update_completedCourse(completedCourseId: int, updated_completedCourse: CompletedCourseUpdate, db: db_dependency):
    return completedCourseService.update_completedCourse(completedCourseId, updated_completedCourse, db)

@router.delete("/{completedCourseId}")
def delete_completedCourse(completedCourseId: int, db: db_dependency):
    return completedCourseService.delete_completedCourse(completedCourseId, db)