from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import mapped_column

from src.models.database.models import Base
from dataclasses import dataclass


@dataclass
class Bottle(Base):
    __tablename__ = "bottles"
    id = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    name = Column(String())
    region = Column(String())
    domain = Column(String())
    wine_type = Column(String())
    year = Column(Integer())
    price = Column(Double())
    photo_link = Column(String())
    shelf_id = mapped_column("shelf_id",Integer(),ForeignKey("shelfs.id"))