import json
from google.genai import errors

def chatResponceHandeler(response1):
    if response1.text is  None:
     print("no responce !!")
    else:
        try:
            parseedObj = json.loads(response1.text);
            print("my Category : " ,parseedObj["category"])
            print("my priority : " ,parseedObj["priority"])
            print("my message : " ,parseedObj["message"])
        except json.JSONDecodeError as e:
            print("not generated as correct josn structure", e)
        except errors.APIError as ae:
            print("problem code :", ae.code)
            print("Error : ", ae)