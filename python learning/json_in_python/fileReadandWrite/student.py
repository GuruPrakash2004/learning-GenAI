import os
import json


current_path = os.path.dirname(os.path.abspath(__file__));

file_path = os.path.join(current_path,"studentDatails.json");


studentDatail = {
    "id": 101,
    "name": "guru",
    "email": "guru123@gmail.com",
    "age": 21
}

print(file_path);

if(os.path.exists(file_path)):
    with open(file_path,"r") as fp:
        student = json.load(fp)
        print(student);

else:
    with open(file_path,"w") as fp:
        json.dump(studentDatail,fp,indent=4)
