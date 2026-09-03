import json
import os

# edit existing file 
script_path = os.path.dirname(os.path.abspath(__file__))
print(script_path);
file_path = os.path.join(script_path,"customers.json")
print(file_path);
with open(file_path, "r") as file:
    customers:dict = json.load(file);

for customer in customers:
    print(customer);


    