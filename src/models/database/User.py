from flask_login import UserMixin
from sqlalchemy import Column, String, Integer
from src.models.database.models import Base
from dataclasses import dataclass


@dataclass
class User(Base, UserMixin):
    __tablename__ = "users"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    id = Column(Integer(), autoincrement=True, nullable=False, primary_key=True)
    username = Column(String(), unique=True)
    password = Column(String())

    def get_id(self):
        return self.id
