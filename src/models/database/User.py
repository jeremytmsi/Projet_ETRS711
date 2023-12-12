from sqlalchemy import Column, String, Integer
from src.models.database.models import Base
from dataclasses import dataclass


@dataclass
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    username = Column(String(), unique=True)
    password = Column(String())
