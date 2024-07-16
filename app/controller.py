import db as db


def get_characters():
    return db.characters


#make it finer
def get_character(character_id: int):
    character = next((char for char in db.characters if char.id == character_id), None)
    return character

def skill_list():
    return "Skill List"