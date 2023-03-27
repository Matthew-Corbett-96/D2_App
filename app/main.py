import logging

import Bungie_API as bungie
from Bungie_Item_Models import Friend
from fastapi import FastAPI
from models import User

app = FastAPI(
    title="Destiny 2 API",
    description="Destiny 2 API",
    version="0.1.0",
    docs_url="/docs"
)


@app.get("/")
def read_root():
    '''
    Test endpoint
    :return: Hello World
    '''
    return {"Hello": "World"}


# @app.get("/getCharacterData")
# def get_data(character: Character) -> dict or None:
#     '''
#     Get Destiny 2 character data from Bungie API
#     :param character: Character object
#     :return: Destiny 2 character data
#     '''

#     try:
#         character_data = bungie.get_destiny2_character_data(
#             character_id=character.character_id,
#             membership_type=character.accountType
#         )
#         print(character_data)
#         return character_data
#     except Exception as exception:
#         print(exception)
#         return None

@app.get("/getProfile")
def get_data(user: User) -> dict or None:
    '''
    Get Bungie Profile data from Bungie API
    :param user: User object
    :return: Bungie Profile data
    '''
    try:
        results = bungie.get_profiles(membership_id=user.bungieMemberId,
                                      membership_type=user.membershipType)
        return results
    except Exception as exception:
        logging.error(exception)
        return None


@app.get("/getFriendsList")
def get_friends_list() -> list[Friend] | None:
    '''
    Get Destiny 2 friends list from Bungie API
    :return: Destiny 2 friends list
    '''
    try:
        friends_list = bungie.getFriendsList()
        return friends_list
    except Exception as exception:
        logging.error(exception)
        return None
