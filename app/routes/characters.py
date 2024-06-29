from fastapi import APIRouter, HTTPException
from typing import List
from models import Character
import db

router = APIRouter()

@router.get("/characters", response_model=List[Character])
def get_characters():
    return db.characters

@router.get("/characters/{character_id}", response_model=Character)
def get_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/characters", response_model=Character)
def create_character(character: Character):
    db.characters.append(character)
    return character

@router.put("/characters/{character_id}", response_model=Character)
def update_character(character_id: int, updated_character: Character):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")

    character.name = updated_character.name
    character.role_id = updated_character.role_id
    character.skill_ids = updated_character.skill_ids
    character.equipment = updated_character.equipment
    return character

@router.delete("/characters/{character_id}", response_model=Character)
def delete_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")

    db.characters.remove(character)
    return character
