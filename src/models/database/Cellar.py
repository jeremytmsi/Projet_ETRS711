from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column
from src.models.database.models import Base
from dataclasses import dataclass


@dataclass
class Cellar(Base):
    __tablename__ = "cellars"

    id = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    name = Column(String())
    available_shelfs = Column(Integer())
    region = Column(String())
    user_id = mapped_column("user_id", Integer(), ForeignKey("users.id"))
