from schema.keyword_mapping import KeywordMappingCreate, KeywordMappingUpdate, KeywordMapping
from database import db_dependency
from fastapi import HTTPException, status


def create_keyword_mapping(new_keyword_mapping: KeywordMappingCreate, db: db_dependency):
    db_keyword_mapping = KeywordMapping(**new_keyword_mapping.dict())
    db.add(db_keyword_mapping)
    db.commit()
    return db_keyword_mapping

def get_keyword_mapping(db: db_dependency):
    keyword_mappings = db.query(KeywordMapping).all()
    return keyword_mappings

def update_keyword_mapping(keyword_mapping_id: int, updated_keyword_mapping: KeywordMappingUpdate, db: db_dependency):
    db_keyword_mapping = db.query(KeywordMapping).filter(keyword_mapping_id == KeywordMapping.keywordMappingId).first()

    if db_keyword_mapping is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_keyword_mapping.dict(exclude_unset=True).items():
        setattr(db_keyword_mapping, key, value)
    
    db.commit()
    return db_keyword_mapping

def delete_keyword_mapping(keyword_mapping_id: int, db: db_dependency):
    db_keyword_mapping = db.query(KeywordMapping).filter(KeywordMapping.keywordMappingId == keyword_mapping_id).first()

    db.delete(db_keyword_mapping)
    db.commit()
    return {"message":"Keyword Mapping Record Deleted Successfully."}