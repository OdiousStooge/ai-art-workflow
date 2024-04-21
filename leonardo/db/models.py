from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True)
    prompt = Column(String)
