from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

router = APIRouter()

# We can use an ORM called SQLAlchemy to use relational dbs with FastAPI
# pip install sqlalchemy

DB_URL = "postgresql://user:password@postgresserver/db"

# create an engine to access the db
engine = create_engine(DB_URL)

# create a session storage
# all the instance of SessionLocal class will act as session storages
SessionLocal = sessionmaker(engine)

# Base is the parent class of all the models that we will create in the project
Base = declarative_base()

# let's create a model for users

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    cart = relationship("cart", ForeignKey("cart.id"))

