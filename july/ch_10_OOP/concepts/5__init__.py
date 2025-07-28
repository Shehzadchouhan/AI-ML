class Employee:
    laguage="python"
    salary="120000"

    def __init__(self,name ,language,salary):
        # putting the valuse in name,language,salary which is passed while creating an object
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getinfo(self):
        print(f"The langaue is {self.laguage}.the salary {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

sheh=Employee("shehzad","python",120000)
print(sheh.name,sheh.language,sheh.salary)
print("\n")
sheh.getinfo()
print("\n")
sheh.greet()
