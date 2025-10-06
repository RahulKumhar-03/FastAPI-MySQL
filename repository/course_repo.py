from schema.course import Course, CourseCreate, CourseUpdate, CourseDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_course(new_course: CourseCreate, db: db_dependency):
    db_course = Course(**new_course.dict())
    db.add(db_course)
    db.commit()
    return db_course

def get_courses(db: db_dependency):
    courses = db.query(Course).all()
    return courses

def update_course(course_id: int, updated_course: CourseUpdate, db: db_dependency):
    db_course = db.query(Course).filter(course_id == Course.courseId).first()

    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_course.dict(exclude_unset=True).items():
        setattr(db_course, key, value)
    
    db.commit()
    return db_course

def delete_course(course_id: int, course_delete: Course, db: db_dependency):
    db_course = db.query(Course).filter(Course.courseId == course_id).first()

    for key, value in course_delete.dict(exclude_unset=True).items():
        setattr(db_course, key, value)
        
    db.commit()
    return {"message":"Course Record Deleted Successfully."}