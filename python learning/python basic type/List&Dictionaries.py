user = {
    "name": "Guru",
    "skills": ["Java", "Python", "AI"],
    "age": 21,
    "contact": {
        "email": "guruprakash832636@gmail.com",
        "phone": 9677597321
        }
    }


print(user["contact"]["email"]);

if "@" in user["contact"]["email"]:
    print("valid email id") 

# skils = ;
for skil in user["skills"]:
    print(skil);