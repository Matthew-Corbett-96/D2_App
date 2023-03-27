

from pydantic import BaseModel
from enum import Enum
from requests import Response

from Bungie_Item_Models import Friend



class BungieResponse(BaseModel):
    '''Base class for Bungie API responses.'''
    Response: dict | None
    ErrorCode: int
    ThrottleSeconds: int
    ErrorStatus: str
    Message: str
    MessageData: dict


class GetFriendsListResponse(BungieResponse):
    '''Response from the GetFriendsList endpoint.'''
    Response: dict[str, list[Friend]] | None
