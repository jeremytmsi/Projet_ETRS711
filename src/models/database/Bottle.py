from sqlalchemy import Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import mapped_column

from src.models.database.models import Base
from dataclasses import dataclass

'''
Représente une bouteille
'''
@dataclass
class Bottle(Base):
    __tablename__ = "bottles"

    def __init__(self, name,region,domain,wine_type,year,price,shelf_id,quantity):
        self.name = name
        self.domain = domain
        self.region = region
        self.wine_type = wine_type
        self.year = year
        self.price = price
        self.shelf_id = shelf_id
        self.quantity = int(quantity)

    id = Column(Integer(), primary_key=True, autoincrement=True, index=True)
    name = Column(String())
    region = Column(String())
    domain = Column(String())
    wine_type = Column(String())
    year = Column(Integer())
    price = Column(Double())
    quantity = Column(Integer())
    shelf_id = mapped_column("shelf_id",Integer(),ForeignKey("shelfs.id",ondelete="CASCADE"))