from repository import project_repo as projectRepo
from database import db_dependency
from schema.project import ProjectCreate, ProjectUpdate

def get_project(db: db_dependency):
    return projectRepo.get_projects(db)

def create_project(new_project: ProjectCreate, db: db_dependency):
    return projectRepo.create_project(new_project, db)

def update_project(projectId: int, updated_project: ProjectUpdate, db: db_dependency):
    return projectRepo.update_project(projectId, updated_project, db)

def delete_project(projectId: int, db: db_dependency):
    return projectRepo.delete_project(projectId, db)