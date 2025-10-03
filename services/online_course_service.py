from repository import online_course_repo as OnlineCourseRepo
from database import db_dependency
from schema.online_course import OnlineCourseCreate, OnlineCourseUpdate

def getOnlineCourses(db: db_dependency):
    return OnlineCourseRepo.get_online_course(db)

def createOnlineCourse(new_online_course: OnlineCourseCreate, db: db_dependency):
    return OnlineCourseRepo.create_online_course(new_online_course, db)

def updateOnlineCourse(onlineCourseId: int, updated_online_course: OnlineCourseUpdate, db: db_dependency):
    return OnlineCourseRepo.update_online_course(onlineCourseId, updated_online_course, db)

def deleteOnlineCourse(onlineCourseId: int, db: db_dependency):
    return OnlineCourseRepo.delete_online_course(onlineCourseId, db)