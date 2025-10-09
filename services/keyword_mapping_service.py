from repository import keyword_mapping_repo as keyword_mapping_repo
from database import db_dependency
from schema.keyword_mapping import KeywordMappingBase, KeywordMappingDelete

def get_keyword_mapping(db: db_dependency):
    return keyword_mapping_repo.get_keyword_mapping(db)

def create_keyword_mapping(new_keyword_mapping: KeywordMappingBase, db: db_dependency, currentUser):
    return keyword_mapping_repo.create_keyword_mapping(new_keyword_mapping, db, currentUser)

def update_keyword_mapping(keyword_mapping_id: int, updated_keyword_mapping: KeywordMappingBase, db: db_dependency, currentUser):
    return keyword_mapping_repo.update_keyword_mapping(keyword_mapping_id, updated_keyword_mapping, db, currentUser)

def delete_keyword_mapping(keyword_mapping_id: int, keywordMapping_delete: KeywordMappingDelete, db: db_dependency, currentUser):
    return keyword_mapping_repo.delete_keyword_mapping(keyword_mapping_id, keywordMapping_delete, db, currentUser)