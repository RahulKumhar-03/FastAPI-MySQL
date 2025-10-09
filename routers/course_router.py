from fastapi import APIRouter
from database import db_dependency
from services import course_service as courseService
from schema.course import CourseCreate, CourseBase, CourseResponse, CourseDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[CourseResponse])
def get_courses(db: db_dependency, user: user_dependency):
    return courseService.getCourses(db)

@router.post("/")
def create_course(new_course: CourseCreate, db: db_dependency, user: user_dependency):
    return courseService.create_course(new_course, db, user)

@router.put("/{courseId}")
def update_course(courseId: int, updated_course: CourseBase, db: db_dependency, user: user_dependency):
    return courseService.update_course(courseId, updated_course, db, user)

@router.delete("/{courseId}")
def delete_course(courseId: int, course_delete: CourseDelete, db: db_dependency, user: user_dependency):
    return courseService.delete_course(courseId, course_delete, db, user)