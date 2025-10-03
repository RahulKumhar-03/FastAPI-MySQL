from schema.certification import Certification, CertificationCreate, CertificationUpdate
from database import db_dependency
from fastapi import HTTPException, status


def create_certification(new_certification: CertificationCreate, db: db_dependency):
    db_certification = Certification(**new_certification.dict())
    db.add(db_certification)
    db.commit()
    return db_certification

def get_certifications(db: db_dependency):
    certifications = db.query(Certification).all()
    return certifications

def update_certification(certification_id: int, updated_certification: CertificationUpdate, db: db_dependency):
    db_certification = db.query(Certification).filter(certification_id == Certification.certificationId).first()

    if db_certification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_certification.dict(exclude_unset=True).items():
        setattr(db_certification, key, value)
    
    db.commit()
    return db_certification

def delete_certification(certification_id: int, db: db_dependency):
    db_certification = db.query(Certification).filter(Certification.certificationId == certification_id).first()

    db.delete(db_certification)
    db.commit()
    return {"message":"Certification Record Deleted Successfully."}