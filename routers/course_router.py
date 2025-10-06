from fastapi import APIRouter
from database import db_dependency
from services import course_service as courseService
from schema.course import CourseCreate, CourseUpdate, CourseResponse, CourseDelete

router = APIRouter()

@router.get("/", response_model=list[CourseResponse])
def get_courses(db: db_dependency):
    return courseService.getCourses(db)

@router.post("/")
def create_course(new_course: CourseCreate, db: db_dependency):
    return courseService.create_course(new_course, db)

@router.put("/{courseId}")
def update_course(courseId: int, updated_course: CourseUpdate, db: db_dependency):
    return courseService.update_course(courseId, updated_course, db)

@router.delete("/{courseId}")
def delete_course(courseId: int, course_delete: CourseDelete, db: db_dependency):
    return courseService.delete_course(courseId, course_delete, db)