class Employee:

    def __init__(self,name, department):
        self.name = name
        self.department = department

    def intro(self):
        print( f"he is {self.name}  from {self.department}")



e1 = Employee("hari","IT")

e1.intro()


