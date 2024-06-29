from fastapi import APIRouter, HTTPException
from typing import List
from models import Role
import db

router = APIRouter()

@router.get("/roles", response_model=List[Role])
def get_roles():
    return db.roles

@router.get("/roles/{role_id}", response_model=Role)
def get_role(role_id: int):
    role = next((r for r in db.roles if r.id == role_id), None)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.post("/roles", response_model=Role)
def create_role(role: Role):
    db.roles.append(role)
    return role
