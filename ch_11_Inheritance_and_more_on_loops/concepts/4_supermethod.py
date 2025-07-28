class Employee:
    def __init__(self):
        print("Contructor of an Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Contructor of an Programmmer")
    b=2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print(Manager.b)
        print("Contructor of an Manager")
    c=3

a=Employee()
print(a.a)

a=Programmer()
print(a.b)

a=Manager()
print(a.c)