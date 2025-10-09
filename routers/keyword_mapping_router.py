from fastapi import APIRouter
from database import db_dependency
from services import keyword_mapping_service as keywordMappingService
from schema.keyword_mapping import KeywordMappingBase, KeywordMappingResponse, KeywordMappingDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[KeywordMappingResponse])
def get_keyword_mapping(db: db_dependency, user: user_dependency):
    return keywordMappingService.get_keyword_mapping(db)

@router.post("/")
def create_keyword_mapping(new_keyword_mapping: KeywordMappingBase, db: db_dependency, user: user_dependency):
    return keywordMappingService.create_keyword_mapping(new_keyword_mapping, db, user)

@router.put("/{keyword_mapping_id}")
def update_keyword_mapping(keyword_mapping_id: int, updated_keyword_mapping: KeywordMappingBase, db: db_dependency, user: user_dependency):
    return keywordMappingService.update_keyword_mapping(keyword_mapping_id, updated_keyword_mapping, db, user)

@router.delete("/{keyword_mapping_id}")
def delete_keyword_mapping(keyword_mapping_id: int, keywordMapping_delete: KeywordMappingDelete, db: db_dependency, user: user_dependency):
    return keywordMappingService.delete_keyword_mapping(keyword_mapping_id, keywordMapping_delete, db, user)