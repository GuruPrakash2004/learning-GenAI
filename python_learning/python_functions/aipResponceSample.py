def send(mgs):
    return  f"{mgs} is recived";

def api_responce(message):
    apicall = send(message);
    mgs = "hi there "
    if( "recived" in apicall):
        responce = {
            "answer" : mgs,
            "intent": "on progress",
            "confidence": 0.72

        }

        return responce;    
    return "no responce";

print( api_responce("helooo !!"));