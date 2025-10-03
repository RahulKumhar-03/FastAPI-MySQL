from repository import completedCourse_repo as completedCourseRepo
from database import db_dependency
from schema.completedCourse import CompletedCourseCreate, CompletedCourseUpdate

def get_completedCourse(db: db_dependency):
    return completedCourseRepo.get_completedCourses(db)

def create_completedCourse(new_completedCourse: CompletedCourseCreate, db: db_dependency):
    return completedCourseRepo.create_completedCourse(new_completedCourse, db)

def update_completedCourse(completedCourseId: int, updated_completedCourse: CompletedCourseUpdate, db: db_dependency):
    return completedCourseRepo.update_completedCourse(completedCourseId, updated_completedCourse, db)

def delete_completedCourse(completedCourseId: int, db: db_dependency):
    return completedCourseRepo.delete_completedCourse(completedCourseId, db)