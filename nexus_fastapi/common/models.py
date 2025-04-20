from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


Base = declarative_base()


class AuditMixIn(Base):
    created_at: Mapped[datetime] = mapped_column(nullable=True)
    created_by: Mapped[int] = mapped_column(nullable=True)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)
    updated_by: Mapped[int] = mapped_column(nullable=True)
    archived_at: Mapped[datetime] = mapped_column(nullable=True)
    archived_by: Mapped[int] = mapped_column(nullable=True)
    unarchived_at: Mapped[datetime] = mapped_column(nullable=True)
    unarchived_by: Mapped[int] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(nullable=True)
    deleted_by: Mapped[int] = mapped_column(nullable=True)
    undeleted_at: Mapped[datetime] = mapped_column(nullable=True)
    undeleted_by: Mapped[int] = mapped_column(nullable=True)

    @property
    def is_archived(self) -> bool:
        return self.archived_at is not None and (self.unarchived_at is None or self.archived_at > self.unarchived_at)

    @is_archived.setter
    def is_archived(self, value: bool) -> None:
        if value:
            self.archived_at = datetime.utcnow()
            self.archived_by = -1
        else:
            self.unarchived_at = datetime.utcnow()
            self.unarchived_by = -1

    @property
    def is_deleted(self) -> bool:
        return self.deleted_at is not None and (self.undeleted_at is None or self.deleted_at > self.undeleted_at)

    @is_deleted.setter
    def is_deleted(self, value: bool) -> None:
        if value:
            self.deleted_at = datetime.utcnow()
            self.deleted_by = -1
        else:
            self.undeleted_at = datetime.utcnow()
            self.undeleted_by = -1
