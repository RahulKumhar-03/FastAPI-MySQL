from repository import keyword_repo as keyword_repo
from database import db_dependency
from schema.keyword import KeywordBase, KeywordDelete

def get_keyword(db: db_dependency):
    return keyword_repo.get_keyword(db)

def create_keyword(new_keyword: KeywordBase, db: db_dependency, currentUser):
    return keyword_repo.create_keyword(new_keyword, db, currentUser)

def update_keyword(keyword_id: int, updated_keyword: KeywordBase, db: db_dependency, currentUser):
    return keyword_repo.update_keyword(keyword_id, updated_keyword, db, currentUser)

def delete_keyword(keyword_id: int, keyword_delete: KeywordDelete, db: db_dependency, currentUser):
    return keyword_repo.delete_keyword(keyword_id, keyword_delete, db, currentUser)