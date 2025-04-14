from sqlalchemy.orm import Session
from .models import NetworkInfrastructure, NetworkArchitecture

def create_network_infrastructure(db: Session, network_id: int, topology: str, devices: list[str]):
    infrastructure = NetworkInfrastructure(
        network_id=network_id,
        topology=topology,
        devices=','.join(devices)
    )
    db.add(infrastructure)
    db.commit()
    db.refresh(infrastructure)
    return infrastructure

def create_network_architecture(db: Session, network_id: int, design: str, protocols: list[str]):
    architecture = NetworkArchitecture(
        network_id=network_id,
        design=design,
        protocols=','.join(protocols)
    )
    db.add(architecture)
    db.commit()
    db.refresh(architecture)
    return architecture