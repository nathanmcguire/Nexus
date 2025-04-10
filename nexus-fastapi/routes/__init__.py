from fastapi import APIRouter

router = APIRouter()

ASSET_CLASSES = {
    "Devices": ["Enterprise Assets", "End-user Devices", "Servers", "IoT Devices", "Network Devices", "Removable Media"],
    "Software": ["Applications", "Operating Systems", "Services", "Libraries", "APIs", "Firmware"],
    "Data": ["Sensitive Data", "Log Data", "Physical Data"],
    "Users": ["Workforce", "Service Providers", "User Accounts", "Administrator Accounts", "Service Accounts"],
    "Network": ["Network Infrastructure", "Network Architecture"],
    "Documentation": ["Plans", "Policies", "Processes", "Procedures"],
}

@router.get("/assets")
def get_asset_classes():
    """
    Returns the CIS Controls Asset Classes and their categories.
    """
    return {"asset_classes": ASSET_CLASSES}