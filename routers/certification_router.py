from fastapi import APIRouter
from database import db_dependency
from services import certification_service as certificationService
from schema.certification import CertificationCreate, CertificationUpdate

router = APIRouter()

@router.get("/")
def getCertification(db: db_dependency):
    return certificationService.getCertifications(db)

@router.post("/")
def createCertification(new_certification: CertificationCreate, db: db_dependency):
    return certificationService.createCertification(new_certification, db)

@router.put("/{certificationId}")
def updateCertification(certificationId: int, updated_certification: CertificationUpdate, db: db_dependency):
    return certificationService.updateCertification(certificationId, updated_certification, db)

@router.delete("/{certificationId}")
def deleteCertification(certificationId: int, db: db_dependency):
    return certificationService.deleteCertification(certificationId, db)