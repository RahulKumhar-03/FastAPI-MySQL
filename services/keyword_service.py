from repository import keyword_repo as keyword_repo
from database import db_dependency
from schema.keyword import KeywordCreate, KeywordUpdate, KeywordDelete

def get_keyword(db: db_dependency):
    return keyword_repo.get_keyword(db)

def create_keyword(new_keyword: KeywordCreate, db: db_dependency):
    return keyword_repo.create_keyword(new_keyword, db)

def update_keyword(keyword_id: int, updated_keyword: KeywordUpdate, db: db_dependency):
    return keyword_repo.update_keyword(keyword_id, updated_keyword, db)

def delete_keyword(keyword_id: int, keyword_delete: KeywordDelete, db: db_dependency):
    return keyword_repo.delete_keyword(keyword_id, keyword_delete, db)