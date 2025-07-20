from pydantic import BaseModel
from typing import Optional

class Song(BaseModel):
    name: str
    path: str
    plays: int = 0

class SongUpdate(BaseModel):
    name: Optional[str]
    path: Optional[str]
    plays: Optional[int]