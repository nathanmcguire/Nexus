from sqlalchemy.orm import Session
from ._M_odels import NetworkInfrastructure, NetworkArchitecture, Network

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

def get_all_network_assets(db: Session):
    return db.query(Network).all()

def create_network_asset(db: Session, network: Network):
    new_network = Network(
        network_type=network.network_type
    )
    db.add(new_network)
    db.commit()
    db.refresh(new_network)
    return new_network

def get_network_asset(db: Session, network_id: int):
    network = db.query(Network).filter(Network.id == network_id).first()
    if not network:
        raise Exception("Network asset not found")
    return network

def update_network_asset(db: Session, network_id: int, network: Network):
    existing_network = db.query(Network).filter(Network.id == network_id).first()
    if not existing_network:
        raise Exception("Network asset not found")
    existing_network.network_type = network.network_type
    db.commit()
    db.refresh(existing_network)
    return existing_network

def delete_network_asset(db: Session, network_id: int):
    network = db.query(Network).filter(Network.id == network_id).first()
    if not network:
        raise Exception("Network asset not found")
    db.delete(network)
    db.commit()