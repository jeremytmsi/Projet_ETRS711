from sqlalchemy.orm import mapped_column
from src.models.database.models import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from dataclasses import dataclass


@dataclass
class Shelf(Base):
    __tablename__ = "shelfs"
    id = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    name = Column(String())
    available_bottles = Column(Integer())
    cellar_id = mapped_column("cellar_id", Integer(), ForeignKey("cellars.id"))