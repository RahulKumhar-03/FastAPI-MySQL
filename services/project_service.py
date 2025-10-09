from repository import project_repo as projectRepo
from database import db_dependency
from schema.project import ProjectCreate, ProjectBase, ProjectDelete

def get_project(db: db_dependency):
    return projectRepo.get_projects(db)

def create_project(new_project: ProjectCreate, db: db_dependency, currentUser):
    return projectRepo.create_project(new_project, db, currentUser)

def update_project(projectId: int, updated_project: ProjectBase, db: db_dependency, currentUser):
    return projectRepo.update_project(projectId, updated_project, db, currentUser)

def delete_project(projectId: int, project_delete: ProjectDelete, db: db_dependency, currentUser):
    return projectRepo.delete_project(projectId, project_delete, db, currentUser)