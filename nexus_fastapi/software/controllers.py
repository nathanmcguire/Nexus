from fastapi import APIRouter, HTTPException, Depends
from typing import List
from .schemas import Software, SoftwareType
from .services import SoftwareService

router = APIRouter(prefix="/software", tags=["Software"])

@router.get("/", response_model=List[Software])
def get_all_software(service: SoftwareService = Depends()):
    return service.get_all_software()

@router.get("/{software_id}", response_model=Software)
def get_software(software_id: int, service: SoftwareService = Depends()):
    software = service.get_software(software_id)
    if not software:
        raise HTTPException(status_code=404, detail="Software not found")
    return software

@router.post("/", response_model=Software)
def create_software(software: Software, service: SoftwareService = Depends()):
    return service.create_software(software)

@router.put("/{software_id}", response_model=Software)
def update_software(software_id: int, software: Software, service: SoftwareService = Depends()):
    updated_software = service.update_software(software_id, software)
    if not updated_software:
        raise HTTPException(status_code=404, detail="Software not found")
    return updated_software

@router.delete("/{software_id}", response_model=dict)
def delete_software(software_id: int, service: SoftwareService = Depends()):
    if not service.delete_software(software_id):
        raise HTTPException(status_code=404, detail="Software not found")
    return {"message": "Software deleted successfully"}