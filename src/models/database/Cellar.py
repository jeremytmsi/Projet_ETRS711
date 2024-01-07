from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.database.models import Base
from dataclasses import dataclass

'''
    Représente une cave
'''
@dataclass
class Cellar(Base):
    __tablename__ = "cellars"

    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id

    id = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    name = Column(String())
    user_id = mapped_column("user_id", Integer(), ForeignKey("users.id"))
