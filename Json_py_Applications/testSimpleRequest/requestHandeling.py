import requests

url = "https://jsonplaceholder.typicode.com/users/9"

""" 
responce = requests.get(url)

if responce.status_code == 200:
    print("request scuccessfull!!")
    print(responce.json())

elif responce.status_code == 404:
     print("request data not found!!")

elif responce.status_code == 500:
     print("serverside erroe!!")

elif responce.status_code == 401:
     print("Authentication problem!!")

else:
    print("some other eror failed!!")
    print(responce.status_code)
 """

try:
    responce = requests.get(url)
    responce.raise_for_status()
    data  = responce.json()
    print(data)
except requests.exceptions.RequestException as e:
     print("API request failed:", e)