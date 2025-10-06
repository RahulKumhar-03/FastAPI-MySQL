from fastapi import APIRouter
from database import db_dependency
from services import online_course_service as OnlineCourseService
from schema.online_course import OnlineCourseCreate, OnlineCourseUpdate, OnlineCourseResponse, OnlineCourseDelete

router = APIRouter()

@router.get("/", response_model=list[OnlineCourseResponse])
def getOnlineCourses(db: db_dependency):
    return OnlineCourseService.getOnlineCourses(db)

@router.post("/")
def createOnlineCourse(new_online_course: OnlineCourseCreate, db: db_dependency):
    return OnlineCourseService.createOnlineCourse(new_online_course, db)

@router.put("/{onlineCourseId}")
def updateOnlineCourse(onlineCourseId: int, updated_online_course: OnlineCourseUpdate, db: db_dependency):
    return OnlineCourseService.updateOnlineCourse(onlineCourseId, updated_online_course, db)

@router.delete("/{onlineCourseId}")
def deleteOnlineCourse(onlineCourseId: int, onlineCourse_delete: OnlineCourseDelete, db: db_dependency):
    return OnlineCourseService.deleteOnlineCourse(onlineCourseId, onlineCourse_delete, db)