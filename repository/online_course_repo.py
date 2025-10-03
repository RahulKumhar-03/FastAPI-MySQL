from schema.online_course import OnlineCourse, OnlineCourseCreate, OnlineCourseUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_online_course(new_onlineCourse: OnlineCourseCreate, db: db_dependency):
    db_onlineCourse = OnlineCourse(**new_onlineCourse.dict())
    db.add(db_onlineCourse)
    db.commit()
    return db_onlineCourse

def get_online_course(db: db_dependency):
    onlineCourses = db.query(OnlineCourse).all()
    return onlineCourses

def update_online_course(online_course_id: int, updated_online_course: OnlineCourseUpdate, db: db_dependency):
    db_online_course = db.query(OnlineCourse).filter(online_course_id == OnlineCourse.onlineCourseId).first()

    if db_online_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_online_course.dict(exclude_unset=True).items():
        setattr(db_online_course, key, value)
    
    db.commit()
    return db_online_course

def delete_online_course(online_course_id: int, db: db_dependency):
    db_online_course = db.query(OnlineCourse).filter(OnlineCourse.onlineCourseId == online_course_id).first()

    db.delete(db_online_course)
    db.commit()
    return {"message":"Online Course Record Deleted Successfully."}