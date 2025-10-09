from repository import certification_repo as certificationRepo
from database import db_dependency
from schema.certification import CertificationCreate, CertificationBase, CertificationDelete

def getCertifications(db: db_dependency):
    return certificationRepo.get_certifications(db)

def createCertification(new_certification: CertificationCreate, db: db_dependency, currentUser):
    return certificationRepo.create_certification(new_certification, db, currentUser)

def updateCertification(certificationId: int, updated_certification: CertificationBase, db: db_dependency, currentUser):
    return certificationRepo.update_certification(certificationId, updated_certification, db, currentUser)

def deleteCertification(certificationId: int, certification_delete: CertificationDelete, db: db_dependency, currentUser):
    return certificationRepo.deleteCertification(certificationId, certification_delete, db. currentUser)