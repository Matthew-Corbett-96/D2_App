from enum import Enum

from pydantic import BaseModel

# make an enum with values for each account type
class AccountType(int, Enum):
    Xbox = 1
    PlayStation = 2
    PC = 3

# Class for Each User
class Character(BaseModel):
    name: str
    accountType: AccountType
    character_id: str
