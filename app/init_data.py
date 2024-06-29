from db import characters, skills, roles
from models import Character, Skill, Role

def init_data():
    roles.append(Role(id=1, name="Rockerboy"))
    roles.append(Role(id=2, name="Solo"))
    roles.append(Role(id=3, name="Netrunner"))
    roles.append(Role(id=4, name="Techie"))
    roles.append(Role(id=5, name="Medtech"))
    roles.append(Role(id=6, name="Media"))
    roles.append(Role(id=7, name="Nomad"))
    

    skills.append(Skill(id=1, name="Charisma"))
    skills.append(Skill(id=2, name="Guitar"))
    skills.append(Skill(id=3, name="Combat"))
    skills.append(Skill(id=4, name="Stealth"))

    characters.append(Character(id=1, name="Johnny Silverhand", role_id=1, skill_ids=[1, 2], equipment=["Guitar", "Pistol"]))
    characters.append(Character(id=2, name="V", role_id=2, skill_ids=[3, 4], equipment=["Katana", "Handgun"]))
