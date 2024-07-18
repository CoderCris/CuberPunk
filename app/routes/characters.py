from fastapi import APIRouter, HTTPException
from typing import List
from models import Character
import controller

router = APIRouter()

@router.get("/characters", response_model=List[Character])
def get_characters():
    return controller.get_characters()

@router.get("/characters/{character_id}", response_model=Character)
def get_character(character_id: int):
    character = controller.get_character(character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/characters", response_model=Character)
def create_character(character: Character):
    return controller.create_character(character)

@router.put("/characters/{character_id}", response_model=Character)
def update_character(character_id: int, updated_character: Character):
    return controller.update_character(character_id, updated_character)

@router.delete("/characters/{character_id}", response_model=Character)
def delete_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")

    db.characters.remove(character)
    return character
