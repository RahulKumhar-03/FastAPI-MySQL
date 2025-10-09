from fastapi import APIRouter
from database import db_dependency
from services import completedCourse_service as completedCourseService
from schema.completedCourse import CompletedCourseCreate, CompletedCourseBase, CompletedCourseResponse, CompletedCourseDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[CompletedCourseResponse])
def get_completedCourse(db: db_dependency, user: user_dependency):
    return completedCourseService.get_completedCourse(db)

@router.post("/")
def create_completedCourse(new_completedCourse: CompletedCourseCreate, db: db_dependency, user: user_dependency):
    return completedCourseService.create_completedCourse(new_completedCourse, db, user)

@router.put("/{completedCourseId}")
def update_completedCourse(completedCourseId: int, updated_completedCourse: CompletedCourseBase, db: db_dependency, user: user_dependency):
    return completedCourseService.update_completedCourse(completedCourseId, updated_completedCourse, db, user)

@router.delete("/{completedCourseId}")
def delete_completedCourse(completedCourseId: int, completedCourse_delete: CompletedCourseDelete, db: db_dependency, user: user_dependency):
    return completedCourseService.delete_completedCourse(completedCourseId, completedCourse_delete, db, user)