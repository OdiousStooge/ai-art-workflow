# flake8: noqa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Prompt

engine = create_engine("sqlite:///prompts.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Add or update a sample prompt
def add_or_update_prompt(id, prompt):
    new_prompt = Prompt(id=id, prompt=prompt)
    session.merge(new_prompt)
    session.commit()


# Add or update a prompts go here

# Example - TODO: REPLACE ME
add_or_update_prompt(
    1,
    "Muscular Orc with a machine gun and goggles and a cigar",
)

add_or_update_prompt(
    2,
    "...next prompt",
)

# End of prompts


# Commit changes
session.commit()
