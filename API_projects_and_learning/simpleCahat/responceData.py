from pydantic import BaseModel
from typing import Literal
from google.genai import errors


class ResponceModel(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    priority: Literal["low","medium","high"]
    message: str

async def responceData(chat, myrequest):

    try:

        response = await chat.send_message(
            myrequest,
            config={
                "response_mime_type": "application/json",
                "response_schema": ResponceModel
            }
        )

        return response

    except errors.ClientError as e:

        print("API Client Error")
        print("Status code:", e.code)
        print("Error:", e)

        return None