from pydantic import BaseModel
from typing import Literal

# SupportResponse Model
class SupportResponse(BaseModel):
    category : Literal["billing", "technical","account","others"]
    priority : Literal["low","medium","high"]
    message: str
