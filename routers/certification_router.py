from fastapi import APIRouter
from database import db_dependency
from services import certification_service as certificationService
from schema.certification import CertificationCreate, CertificationBase, CertificationResponse, CertificationDelete
from services.auth_service import user_dependency

router = APIRouter()

@router.get("/", response_model=list[CertificationResponse])
def getCertification(db: db_dependency, user: user_dependency):
    return certificationService.getCertifications(db)

@router.post("/")
def createCertification(new_certification: CertificationCreate, db: db_dependency, user: user_dependency):
    return certificationService.createCertification(new_certification, db, user)

@router.put("/{certificationId}")
def updateCertification(certificationId: int, updated_certification: CertificationBase, db: db_dependency, user: user_dependency):
    return certificationService.updateCertification(certificationId, updated_certification, db, user)

@router.delete("/{certificationId}")
def deleteCertification(certificationId: int, certification_delete: CertificationDelete, db: db_dependency, user: user_dependency):
    return certificationService.deleteCertification(certificationId, certification_delete, db, user)