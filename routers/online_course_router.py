from fastapi import APIRouter
from database import db_dependency
from services import online_course_service as OnlineCourseService
from schema.online_course import OnlineCourseCreate, OnlineCourseBase, OnlineCourseResponse, OnlineCourseDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[OnlineCourseResponse])
def getOnlineCourses(db: db_dependency, user: user_dependency):
    return OnlineCourseService.getOnlineCourses(db)

@router.post("/")
def createOnlineCourse(new_online_course: OnlineCourseCreate, db: db_dependency, user: user_dependency):
    return OnlineCourseService.createOnlineCourse(new_online_course, db, user)

@router.put("/{onlineCourseId}")
def updateOnlineCourse(onlineCourseId: int, updated_online_course: OnlineCourseBase, db: db_dependency, user: user_dependency):
    return OnlineCourseService.updateOnlineCourse(onlineCourseId, updated_online_course, db, user)

@router.delete("/{onlineCourseId}")
def deleteOnlineCourse(onlineCourseId: int, onlineCourse_delete: OnlineCourseDelete, db: db_dependency, user: user_dependency):
    return OnlineCourseService.deleteOnlineCourse(onlineCourseId, onlineCourse_delete, db, user)