from repository import course_repo as courseRepo
from database import db_dependency
from schema.course import CourseCreate, CourseBase, CourseDelete

def getCourses(db: db_dependency):
    return courseRepo.get_courses(db)

def create_course(new_course: CourseCreate, db: db_dependency, currentUser):
    return courseRepo.create_course(new_course, db, currentUser)

def update_course(courseId: int, updated_course: CourseBase, db: db_dependency, currentUser):
    return courseRepo.update_course(courseId, updated_course, db, currentUser)

def delete_course(courseId: int, course_delete: CourseDelete, db: db_dependency, currentUser):
    return courseRepo.delete_course(courseId, course_delete, db, currentUser)