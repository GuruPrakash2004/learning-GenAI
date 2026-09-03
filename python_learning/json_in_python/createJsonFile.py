import os
import json


current_path = os.path.dirname(os.path.abspath(__file__));
file_path = os.path.join(current_path,"createJsonCustomer.json");

myCustomer =   {
    "id": 101,
    "name": "Alex Mercer",
    "email": "alex.mercer@example.com",
    "city": "Bengaluru"
  }

with open(file_path,"w") as fp:
    json.dump(myCustomer,fp,indent=4);

