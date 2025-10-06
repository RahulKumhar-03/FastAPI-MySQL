from fastapi import APIRouter
from database import db_dependency
from services import keyword_service as keywordService
from schema.keyword import KeywordCreate, KeywordUpdate, KeywordResponse

router = APIRouter()

@router.get("/", response_model=list[KeywordResponse])
def get_keyword(db: db_dependency):
    return keywordService.get_keyword(db)

@router.post("/")
def create_keyword(new_keyword: KeywordCreate, db: db_dependency):
    return keywordService.create_keyword(new_keyword, db)

@router.put("/{keyword_id}")
def update_keyword(keyword_id: int, updated_keyword: KeywordUpdate, db: db_dependency):
    return keywordService.update_keyword(keyword_id, updated_keyword, db)

@router.delete("/{keyword_id}")
def delete_keyword(keyword_id: int, db: db_dependency):
    return keywordService.delete_keyword(keyword_id, db)