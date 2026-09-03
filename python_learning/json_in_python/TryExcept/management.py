import json
import os


cuurent_path = os.path.dirname(os.path.abspath(__file__));

file_path = os.path.join(cuurent_path,"management.json");

manager = {
    "name": "random",
    "age": 22
}

try:
    if(os.path.exists(file_path)):
        with open(file_path,"r") as fp:
            manage = json.load(fp)
            print("the--------manager---------- details-------------")
            print(manage)
    else:
        with open(file_path,"w") as fp:
            json.dump(manager,fp,indent=4)
            print("File didn't exist, so a new one was created!")

except FileNotFoundError as e:
    print("the "+e.filename+" is not exist");

except json.JSONDecodeError as de:
    print("The file exists but has corrupted or badly formatted JSON data.")

else:
    print("successfull")

finally:
    print("all process are done!");
