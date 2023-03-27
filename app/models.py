from pydantic import BaseModel

# Class for Each User
class Character(BaseModel):
    name: str
    accountType: int
    character_id: str
