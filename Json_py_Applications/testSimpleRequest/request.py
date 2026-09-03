import requests
from pydantic import BaseModel

# class responceModel(BaseModel):
#     id: int
#     name: str
#     username: str
#     email: str


# get responce from API server
url = "https://jsonplaceholder.typicode.com/users/1"
responce = requests.get(url) 
# data = responceModel.model_validate(responce.json());
# print(data.email)
# .jon() -> conver the json string into python object dictionaries
dictResponce = responce.json();
print(dictResponce["name"])
# print(dictResponce.status_code)

# post 
print("--------------post----------------")

mydata = {
    "title": "Learning GenAI",
    "body": "I am learning API communication",
    "userId": 1
}

posturl = "https://jsonplaceholder.typicode.com/posts"

postResp = requests.post(posturl, json=mydata)

print(postResp.status_code)
data =postResp.json()
print(data["body"]);



