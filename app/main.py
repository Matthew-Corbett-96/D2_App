from fastapi import FastAPI
# import get_destiny2_character_data function from Bungie_API.py
from Bungie_API import get_destiny2_character_data
# import models
from models import Character

app = FastAPI(
    title="Destiny 2 API",
    description="Destiny 2 API",
    version="0.1.0",
    docs_url="/docs",
)

@app.get("/")
def read_root():
    '''
    Test endpoint
    :return: Hello World
    '''
    return {"Hello": "World"}


@app.get("/getCharacterData")
def get_data(character: Character) -> dict or None:
    '''
    Get Destiny 2 character data from Bungie API
    :param character: Character object
    :return: Destiny 2 character data
    '''

    try:
        character_data = get_destiny2_character_data(
            character_id=character.character_id,
            membership_type=character.accountType
        )
        print(character_data)
        return character_data
    except Exception as exception:
        print(exception)
        return None
