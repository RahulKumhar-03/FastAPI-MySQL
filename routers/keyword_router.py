from fastapi import APIRouter
from database import db_dependency
from services import keyword_service as keywordService
from schema.keyword import KeywordBase, KeywordResponse, KeywordDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[KeywordResponse])
def get_keyword(db: db_dependency, user: user_dependency):
    return keywordService.get_keyword(db)

@router.post("/")
def create_keyword(new_keyword: KeywordBase, db: db_dependency, user: user_dependency):
    return keywordService.create_keyword(new_keyword, db, user)

@router.put("/{keyword_id}")
def update_keyword(keyword_id: int, updated_keyword: KeywordBase, db: db_dependency, user: user_dependency):
    return keywordService.update_keyword(keyword_id, updated_keyword, db, user)

@router.delete("/{keyword_id}")
def delete_keyword(keyword_id: int, keyword_delete: KeywordDelete, db: db_dependency, user: user_dependency):
    return keywordService.delete_keyword(keyword_id, keyword_delete, db, user)