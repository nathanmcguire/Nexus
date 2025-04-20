from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from database import Base
from common.models import AuditMixIn


class User(Base, AuditMixIn):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    guid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
