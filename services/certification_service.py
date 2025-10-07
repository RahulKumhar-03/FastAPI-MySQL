from repository import certification_repo as certificationRepo
from database import db_dependency
from schema.certification import CertificationCreate, CertificationUpdate, CertificationDelete

def getCertifications(db: db_dependency):
    return certificationRepo.get_certifications(db)

def createCertification(new_certification: CertificationCreate, db: db_dependency):
    return certificationRepo.create_certification(new_certification, db)

def updateCertification(certificationId: int, updated_certification: CertificationUpdate, db: db_dependency):
    return certificationRepo.update_certification(certificationId, updated_certification, db)

def deleteCertification(certificationId: int, certification_delete: CertificationDelete, db: db_dependency):
    return certificationRepo.deleteCertification(certificationId, certification_delete, db)