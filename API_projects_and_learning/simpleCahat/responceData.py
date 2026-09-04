from pydantic import BaseModel
from typing import Literal

class ResponceModel(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    priority: Literal["low","medium","high"]
    message: str

async def responceData(chat,myrequest):
        response = await chat.send_message(
        f"{myrequest}"
        ,
        config={
        "response_mime_type": "application/json",
        "response_schema": ResponceModel
        }
        )
        return response