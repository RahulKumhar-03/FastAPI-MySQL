from fastapi import APIRouter
from database import db_dependency
from services import project_service as projectService
from schema.project import ProjectCreate, ProjectBase, ProjectResponse, ProjectDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[ProjectResponse])
def get_project(db: db_dependency, user: user_dependency):
    return projectService.get_project(db)

@router.post("/")
def create_project(new_project: ProjectCreate, db: db_dependency, user: user_dependency):
    return projectService.create_project(new_project, db, user)

@router.put("/{projectId}")
def update_project(projectId: int, updated_project: ProjectBase, db: db_dependency, user: user_dependency):
    return projectService.update_project(projectId, updated_project, db, user)

@router.delete("/{projectId}")
def delete_project(projectId: int, project_delete: ProjectDelete, db: db_dependency, user: user_dependency):
    return projectService.delete_project(projectId, project_delete, db, user_dependency)