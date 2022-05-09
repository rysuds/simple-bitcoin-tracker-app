from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field


class UserEmail(BaseModel):
    email: str

class UserAddress(BaseModel):
    address: str
