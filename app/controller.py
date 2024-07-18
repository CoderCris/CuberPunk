import db as db


def get_characters():
    return db.characters


#make it finer
def get_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    return character

def create_character(character):
    db.characters.append(character)
    return character

#make it finer
def update_character(character_id: int, updated_character):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        return None

    character.name = updated_character.name
    character.role_id = updated_character.role_id
    character.skill_ids = updated_character.skill_ids
    character.equipment = updated_character.equipment
    return character

def delete_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    if character is None:
        return None

    db.characters.remove(character)
    return character

def search_character_by_name(name: str):
    return [char for char in db.characters if char.name == name]

def skill_list():
    return "Skill List"