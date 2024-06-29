from pydantic import BaseModel
from typing import List, Optional

class Skill(BaseModel):
    id: int
    name: str

class Role(BaseModel):
    id: int
    name: str

class Character(BaseModel):
    id: int
    name: str
    role_id: int
    skill_ids: List[int]
    #equipment: Optional[List[str]] = []
