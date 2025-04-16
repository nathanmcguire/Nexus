from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TimestampMixin():
    created_at: datetime
    created_by: int
    updated_at: datetime
    updated_by: int
    deleted_at: datetime
    deleted_by: int
    recovered_at: datetime
    recovered_by: int