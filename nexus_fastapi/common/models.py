from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class Audit:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.utcnow, nullable=False)

    @declared_attr
    def created_by(cls):
        return Column(String, nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=True)

    @declared_attr
    def updated_by(cls):
        return Column(String, nullable=True)

    @declared_attr
    def archived_at(cls):
        return Column(DateTime, nullable=True)

    @declared_attr
    def archived_by(cls):
        return Column(String, nullable=True)

    @declared_attr
    def unarchived_at(cls):
        return Column(DateTime, nullable=True)

    @declared_attr
    def unarchived_by(cls):
        return Column(String, nullable=True)

    @property
    def is_archived(self):
        return self.archived_at is not None and (self.unarchived_at is None or self.archived_at > self.unarchived_at)

    @declared_attr
    def deleted_at(cls):
        return Column(DateTime, nullable=True)

    @declared_attr
    def deleted_by(cls):
        return Column(String, nullable=True)
    
    @declared_attr
    def undeleted_at(cls):
        return Column(DateTime, nullable=True)

    @declared_attr
    def undeleted_by(cls):
        return Column(String, nullable=True)

    @property
    def is_deleted(self):
        return self.deleted_at is not None and (self.recovered_at is None or self.deleted_at > self.undeleted_at)

