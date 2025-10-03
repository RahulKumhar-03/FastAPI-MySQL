from repository import course_repo as courseRepo
from database import db_dependency
from schema.course import CourseCreate, CourseUpdate

def getCourses(db: db_dependency):
    return courseRepo.get_courses(db)

def create_course(new_course: CourseCreate, db: db_dependency):
    return courseRepo.create_course(new_course, db)

def update_course(courseId: int, updated_course: CourseUpdate, db: db_dependency):
    return courseRepo.update_course(courseId, updated_course, db)

def delete_course(courseId: int, db: db_dependency):
    return courseRepo.delete_course(courseId, db)