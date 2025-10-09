from repository import completedCourse_repo as completedCourseRepo
from database import db_dependency
from schema.completedCourse import CompletedCourseCreate, CompletedCourseBase, CompletedCourseDelete

def get_completedCourse(db: db_dependency):
    return completedCourseRepo.get_completedCourses(db)

def create_completedCourse(new_completedCourse: CompletedCourseCreate, db: db_dependency, currentUser):
    return completedCourseRepo.create_completedCourse(new_completedCourse, db, currentUser)

def update_completedCourse(completedCourseId: int, updated_completedCourse: CompletedCourseBase, db: db_dependency, currentUser):
    return completedCourseRepo.update_completedCourse(completedCourseId, updated_completedCourse, db, currentUser)

def delete_completedCourse(completedCourseId: int, completedCourse_delete: CompletedCourseDelete, db: db_dependency, currentUser):
    return completedCourseRepo.delete_completedCourse(completedCourseId, completedCourse_delete, db, currentUser)