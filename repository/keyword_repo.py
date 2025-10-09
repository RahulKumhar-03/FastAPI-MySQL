from schema.keyword import KeywordBase , Keyword, KeywordDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_keyword(new_keyword: KeywordBase, db: db_dependency, currentUser):
    db_keyword = Keyword(**new_keyword.model_dump(), createdBy = currentUser["userId"])
    db.add(db_keyword)
    db.commit()
    return db_keyword

def get_keyword(db: db_dependency):
    keywords = db.query(Keyword).all()
    return keywords

def update_keyword(keyword_id: int, updated_keyword: KeywordBase, db: db_dependency, currentUser):
    db_keyword = db.query(Keyword).filter(keyword_id == Keyword.keywordId).first()

    if db_keyword is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_keyword.model_dump().items():
        setattr(db_keyword, key, value)

    db_keyword.changedBy = currentUser["userId"]
    
    db.commit()
    return db_keyword

def delete_keyword(keyword_id: int, keyword_delete: KeywordDelete, db: db_dependency, currentUser):
    db_keyword = db.query(Keyword).filter(Keyword.keywordId == keyword_id).first()

    for key, value in keyword_delete.model_dump().items():
        setattr(db_keyword, key, value)
        
    db_keyword.deletedBy = currentUser["userId"]

    db.commit()
    return {"message":"Keyword Record Deleted Successfully."}