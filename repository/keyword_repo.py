from schema.keyword import KeywordCreate, KeywordUpdate, Keyword
from database import db_dependency
from fastapi import HTTPException, status


def create_keyword(new_keyword: KeywordCreate, db: db_dependency):
    db_keyword = Keyword(**new_keyword.dict())
    db.add(db_keyword)
    db.commit()
    return db_keyword

def get_keyword(db: db_dependency):
    keywords = db.query(Keyword).all()
    return keywords

def update_keyword(keyword_id: int, updated_keyword: KeywordUpdate, db: db_dependency):
    db_keyword = db.query(Keyword).filter(keyword_id == Keyword.keywordId).first()

    if db_keyword is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_keyword.dict(exclude_unset=True).items():
        setattr(db_keyword, key, value)
    
    db.commit()
    return db_keyword

def delete_keyword(keyword_id: int, db: db_dependency):
    db_keyword = db.query(Keyword).filter(Keyword.keywordId == keyword_id).first()

    db.delete(db_keyword)
    db.commit()
    return {"message":"Keyword Record Deleted Successfully."}