names = ["guru", "hari", "raju", "hellen","mary"];
# list are mutable
names[1] = "nadish";
print(names);

names.insert(2,"Gopal");
print(names);

names.append("hari");
print(names);


names.sort();
print(names);

names.remove("hari");
print(names);
