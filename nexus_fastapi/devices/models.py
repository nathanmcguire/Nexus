from fastapi.domains.assets.models import Asset

class Device(Asset):
    """Base class for all devices."""
    pass

class EndUserDevice(Device):
    """Devices used by end-users."""
    pass

class Server(Device):
    """Server devices."""
    pass

class IoTDevice(Device):
    """Internet of Things devices."""
    pass

class NonComputingDevice(Device):
    """Devices that are not computing devices."""
    pass

class NetworkDevice(Device):
    """Devices used in networking."""
    pass

class RemovableMedia(Device):
    """Removable media devices."""
    pass