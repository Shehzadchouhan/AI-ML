class Employee:
    language="python" #This is a class attribute
    salary=120000

    def getinfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}",)

    @staticmethod
    def greet():
        print("good morning")

sheh=Employee()
sheh.getinfo()
sheh.greet()


