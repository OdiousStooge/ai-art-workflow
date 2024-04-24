import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from db.models import Base, Prompt
from util.leo import leo_magick
from util.leo import leo_realism

# Set up logging
logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load environment variables
load_dotenv()

# Constants
# TODO: Set the range of prompts to generate Start and End inclusive corresponds to ids in prompts.db
START = 1  # start of the range
END = 6  # end of the range (inclusive)
PROMPT_ID = list(range(START, END + 1))
# TODO: Set the core theme that will be concatenated to each prompt
CORE_THEME = """
in the style of [add core theme prompt here]
"""  # noqa

# TODO: Set to True to run in realism mode (photo real) False to run in magick mode (stylized)
RUN_REALISM = False

# Set up database connection
engine = create_engine("sqlite:///prompts.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def main():
    logging.info("Starting main function")

    for prompt_id in PROMPT_ID:
        # Query for the prompt
        prompt = session.query(Prompt).get(prompt_id)
        if prompt is None:
            logging.error(f"No prompt found with id {prompt_id}")
            return

        if RUN_REALISM:
            logging.info("Running in realism mode")
            response = leo_realism(prompt.prompt, CORE_THEME)
        else:
            logging.info("Running in magick mode")
            response = leo_magick(prompt.prompt, CORE_THEME)

    logging.info(f"Received response {response}")
    logging.info("Finished main function")


if __name__ == "__main__":
    main()
