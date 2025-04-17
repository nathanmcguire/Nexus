from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Audit(BaseModel):
    created_at: datetime
    created_by: int
    updated_at: Optional[datetime] = Field(default=None, nullable=True)
    updated_by: Optional[int] = Field(default=None, nullable=True)
    archived_at: Optional[datetime] = Field(default=None, nullable=True)
    archived_by: Optional[int] = Field(default=None, nullable=True)
    unarchived_at: Optional[datetime] = Field(default=None, nullable=True)
    unarchived_by: Optional[int] = Field(default=None, nullable=True)
    is_archived: bool
    deleted_at: Optional[datetime] = Field(default=None, nullable=True)
    deleted_by: Optional[int] = Field(default=None, nullable=True)
    undeleted_at: Optional[datetime] = Field(default=None, nullable=True)
    undeleted_by: Optional[int] = Field(default=None, nullable=True)
    is_deleted: bool