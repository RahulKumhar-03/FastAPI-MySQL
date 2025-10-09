from schema.course import Course, CourseCreate, CourseBase, CourseDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_course(new_course: CourseCreate, db: db_dependency, currentUser):
    db_course = Course(
        **new_course.model_dump(),
        createdBy = currentUser["userId"]    
    )
    db.add(db_course)
    db.commit()
    return db_course

def get_courses(db: db_dependency):
    courses = db.query(Course).all()
    return courses

def update_course(course_id: int, updated_course: CourseBase, db: db_dependency, currentUser):
    db_course = db.query(Course).filter(course_id == Course.courseId).first()

    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_course.model_dump().items():
        setattr(db_course, key, value)

    db_course.changedBy = currentUser["userId"]
    
    db.commit()
    return db_course

def delete_course(course_id: int, course_delete: Course, db: db_dependency, currentUser):
    db_course = db.query(Course).filter(Course.courseId == course_id).first()

    for key, value in course_delete.model_dump().items():
        setattr(db_course, key, value)

    db_course.deletedBy = currentUser["userId"]
        
    db.commit()
    return {"message":"Course Record Deleted Successfully."}