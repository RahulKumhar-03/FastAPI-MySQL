from fastapi import APIRouter
from database import db_dependency
from services import keyword_mapping_service as keywordMappingService
from schema.keyword_mapping import KeywordMappingCreate, KeywordMappingUpdate

router = APIRouter()

@router.get("/")
def get_keyword_mapping(db: db_dependency):
    return keywordMappingService.get_keyword_mapping(db)

@router.post("/")
def create_keyword_mapping(new_keyword_mapping: KeywordMappingCreate, db: db_dependency):
    return keywordMappingService.create_keyword_mapping(new_keyword_mapping, db)

@router.put("/{keyword_mapping_id}")
def update_keyword_mapping(keyword_mapping_id: int, updated_keyword_mapping: KeywordMappingUpdate, db: db_dependency):
    return keywordMappingService.update_keyword_mapping(keyword_mapping_id, updated_keyword_mapping, db)

@router.delete("/{keyword_mapping_id}")
def delete_keyword_mapping(keyword_mapping_id: int, db: db_dependency):
    return keywordMappingService.delete_keyword_mapping(keyword_mapping_id, db)