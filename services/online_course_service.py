from repository import online_course_repo as OnlineCourseRepo
from database import db_dependency
from schema.online_course import OnlineCourseCreate, OnlineCourseBase, OnlineCourseDelete

def getOnlineCourses(db: db_dependency):
    return OnlineCourseRepo.get_online_course(db)

def createOnlineCourse(new_online_course: OnlineCourseCreate, db: db_dependency, currentUser):
    return OnlineCourseRepo.create_online_course(new_online_course, db, currentUser)

def updateOnlineCourse(onlineCourseId: int, updated_online_course: OnlineCourseBase, db: db_dependency, currentUser):
    return OnlineCourseRepo.update_online_course(onlineCourseId, updated_online_course, db, currentUser)

def deleteOnlineCourse(onlineCourseId: int, onlineCourse_delete: OnlineCourseDelete, db: db_dependency, currentUser):
    return OnlineCourseRepo.delete_online_course(onlineCourseId, onlineCourse_delete, db, currentUser)