from schema.project import Project, ProjectCreate, ProjectUpdate, ProjectDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_project(new_project: ProjectCreate, db: db_dependency):
    db_project = Project(**new_project.model_dump())
    db.add(db_project)
    db.commit()
    return db_project

def get_projects(db: db_dependency):
    projects = db.query(Project).all()
    return projects

def update_project(project_id: int, updated_project: ProjectUpdate, db: db_dependency):
    db_project = db.query(Project).filter(project_id == Project.projectId).first()

    if db_project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_project.model_dump().items():
        setattr(db_project, key, value)
    
    db.commit()
    return db_project

def delete_project(project_id: int, project_delete: ProjectDelete, db: db_dependency):
    db_project = db.query(Project).filter(Project.projectId == project_id).first()

    for key, value in project_delete.model_dump().items():
        setattr(db_project, key, value)
        
    db.commit()
    return {"message":"Project Record Deleted Successfully."}