import json;

user = {
    "name": "Guru",
    "skills": ["Java", "Python", "AI"],
    "age": 21,
    "contact": {
        "email": "guruprakash832636@gmail.com",
        "phone": 9677597321
        }
    }

# to convert dict -> json strings we use dumps
dictToJson = json.dumps(user);
print(type(dictToJson));
#  to convert json -> dict strings we use loads
JsonToDict = json.loads(dictToJson);
print(type(JsonToDict));


print(type({"name": "Guru"}))