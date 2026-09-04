
#  => *args
def manyargs(*args):
    mytup = args
    print(type(mytup))
    print(*args)


manyargs(1,2,3,4,5)

#  => *kwargs
def keyValues(**kwargs):
    my = kwargs
    print(type(my))
    print(my)

keyValues(
    name = "Guru",
    department = "IT"
)