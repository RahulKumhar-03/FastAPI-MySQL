from schema.certification import Certification, CertificationCreate, CertificationBase, CertificationDelete
from database import db_dependency
from fastapi import HTTPException, status


def create_certification(new_certification: CertificationCreate, db: db_dependency, currentUser):
    db_certification = Certification(
        **new_certification.model_dump(),
        createdBy = currentUser["userId"]
    )
    db.add(db_certification)
    db.commit()
    return db_certification

def get_certifications(db: db_dependency):
    certifications = db.query(Certification).all()
    return certifications

def update_certification(certification_id: int, updated_certification: CertificationBase, db: db_dependency, currentUser):
    db_certification = db.query(Certification).filter(certification_id == Certification.certificationId).first()

    if db_certification is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NO Record Found")

    for key, value in updated_certification.model_dump().items():
        setattr(db_certification, key, value)

    db_certification.changedBy = currentUser["userId"]
    
    db.commit()
    return db_certification

def delete_certification(certification_id: int, certification_delete: CertificationDelete, db: db_dependency, currentUser):
    db_certification = db.query(Certification).filter(Certification.certificationId == certification_id).first()

    for key, value in certification_delete.model_dump().items():
        setattr(db_certification, key, value)

    db_certification.deletedBy = currentUser["userId"]
        
    db.commit()
    return {"message":"Certification Record Deleted Successfully."}