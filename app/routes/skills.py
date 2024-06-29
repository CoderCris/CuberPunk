from fastapi import APIRouter, HTTPException
from typing import List
from models import Skill
import db

router = APIRouter()

@router.get("/skills", response_model=List[Skill])
def get_skills():
    return db.skills

@router.get("/skills/{skill_id}", response_model=Skill)
def get_skill(skill_id: int):
    skill = next((s for s in db.skills if s.id == skill_id), None)
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.post("/skills", response_model=Skill)
def create_skill(skill: Skill):
    db.skills.append(skill)
    return skill
