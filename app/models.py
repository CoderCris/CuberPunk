from pydantic import BaseModel
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship



class Base(DeclarativeBase):
    pass

class User(BaseModel):
    _tablename_ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(70))

class Skill(BaseModel):
    _tablename_ = 'skills'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

class Role(BaseModel):
    _tablename_ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

class Character(BaseModel):
    _tablename_ = 'characters'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'))
    skill_ids: Mapped[List[int]] = mapped_column(List[int], ForeignKey('skills.id'))

