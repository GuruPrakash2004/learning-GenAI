
def aipResponce(mgs):
    message= "get the credentials from the server";

    if "answer" in mgs:
        responce = {
            "intent": "responce",
            "message": message,
            "confidence": 0.92
        }

        return responce;

    return "server side error"