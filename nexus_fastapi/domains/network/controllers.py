from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .services import create_network_infrastructure, create_network_architecture
from .schemas import NetworkInfrastructure, NetworkArchitecture
from ...database import get_db

router = APIRouter(prefix="/network", tags=["Network"])

@router.post("/infrastructure", response_model=NetworkInfrastructure)
def add_network_infrastructure(
    network_id: int,
    infrastructure: NetworkInfrastructure,
    db: Session = Depends(get_db)
):
    return create_network_infrastructure(
        db,
        network_id,
        infrastructure.topology,
        infrastructure.devices
    )

@router.post("/architecture", response_model=NetworkArchitecture)
def add_network_architecture(
    network_id: int,
    architecture: NetworkArchitecture,
    db: Session = Depends(get_db)
):
    return create_network_architecture(
        db,
        network_id,
        architecture.design,
        architecture.protocols
    )