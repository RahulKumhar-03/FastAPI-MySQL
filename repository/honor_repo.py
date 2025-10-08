from schema.honor import Honor, HonorCreate, HonorUpdate, HonorDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_honor(new_honor: HonorCreate, db: db_dependency):
    db_honor = Honor(**new_honor.model_dump())
    db.add(db_honor)
    db.commit()
    return db_honor

def get_honors(db: db_dependency):
    honors = db.query(Honor).all()
    return honors

def update_honor(honor_id: int, updated_honor: HonorUpdate, db: db_dependency):
    db_honor = db.query(Honor).filter(honor_id == Honor.honorId).first()

    if db_honor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_honor.model_dump().items():
        setattr(db_honor, key, value)
    
    db.commit()
    return db_honor

def delete_honor(honor_id: int, honor_delete: HonorDelete, db: db_dependency):
    db_honor = db.query(Honor).filter(Honor.honorId == honor_id).first()

    for key, value in honor_delete.model_dump().items():
        setattr(db_honor, key, value)
        
    db.commit()
    return {"message":"Honor Record Deleted Successfully."}