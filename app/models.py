from enum import Enum
from pydantic import BaseModel


# Bungie Profile Class
class Profile(BaseModel):
    name: str
    membership_id: str
    membership_type: int

# Class for Each User
class User(BaseModel):
    name: str
    membershipType: int
    bungieMemberId: str
