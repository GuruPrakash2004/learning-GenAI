
number = [1,2,3,4,5,6,7];

# basic
newList = []
for num in number:
    newList.append(num)

print(newList)

comperhensionList = [num for num in number if num%2 ==0]

print(comperhensionList)


messages = [ "this " ," I wish ", "HE is so Dramitic"]

cleanMgs = [mgs.lower().strip() for mgs in messages]
print(cleanMgs)

objMgs = {
         i+1 :  mgs.strip().lower()  for i,mgs in enumerate(messages) 
}

print(objMgs)

