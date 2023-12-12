from sqlalchemy.orm import declarative_base

Base = declarative_base()

import src.models.database.User
import src.models.database.Cellar
import src.models.database.Shelf