from schema.completedCourse import CompletedCourse, CompletedCourseCreate, CompletedCourseUpdate, CompletedCourseDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_completedCourse(new_completedCourse: CompletedCourseCreate, db: db_dependency):
    db_completedCourse = CompletedCourse(**new_completedCourse.model_dump())
    db.add(db_completedCourse)
    db.commit()
    return db_completedCourse

def get_completedCourses(db: db_dependency):
    completedCourses = db.query(CompletedCourse).all()
    return completedCourses

def update_completedCourse(completedCourse_id: int, updated_completedCourse: CompletedCourseUpdate, db: db_dependency):
    db_completedCourse = db.query(CompletedCourse).filter(completedCourse_id == CompletedCourse.completedCourseId).first()

    if db_completedCourse is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_completedCourse.model_dump().items():
        setattr(db_completedCourse, key, value)
    
    db.commit()
    return db_completedCourse

def delete_completedCourse(completedCourse_id: int, completedCourseDelete: CompletedCourseDelete, db: db_dependency):
    db_completedCourse = db.query(CompletedCourse).filter(CompletedCourse.completedCourseId == completedCourse_id).first()

    for key, value in completedCourseDelete.model_dump().items():
        setattr(db_completedCourse, key, value)

    db.commit()
    return {"message":"Completed Course Record Deleted Successfully."}