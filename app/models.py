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


# commit message based on changes 
# 1. added Bungie_API_Models.py
# 2. added Bungie_API.py
# 3. added Bungie_Enums.py
# 4. added Bungie_Item_Models.py
