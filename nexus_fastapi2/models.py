from sqlalchemy.orm import declarative_base
Base = declarative_base()
# models must be imported after base is defined.
from .users.models import User