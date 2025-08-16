from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Script(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    language: str
    message: str