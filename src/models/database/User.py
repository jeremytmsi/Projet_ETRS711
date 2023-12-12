from sqlalchemy import Column, String, Integer
from src.models.database.models import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer(),primary_key=True,index=True,autoincrement=True,nullable=False)
    username = Column(String(),primary_key=True,unique=True)
    password = Column(String())