import requests


url = "http://127.0.0.1:8000/employees"

header ={
    "Authorization" : "Bearer abc123xyz"
}

responce = requests.get(url, headers=header)

print("---------------employeee---------------------------")
print("Get Json Responce ",responce.json());


# Test POST create employee
new_data = {
    "name": "Prakash",
    "department": "DevOps",
    "leave_balance": 10
}
post_response = requests.post(url, json=new_data, headers=header)
print("---------------employeee-------------created--------")
print("POST Response:", post_response.json())