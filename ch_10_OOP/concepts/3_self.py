class Employee:
    language="python" #This is a class attribute
    salary=120000

    def getinfo(self): #convetionol atrgument for automatic give parameter
        print(f"the language is {self.language}.the salary is {self.salary}",)

    def greet(self):
        print("good morning")

sheh=Employee()
# sheh.language="js"
sheh.getinfo()
# sheh.getinfo(sheh) #actually the above line is this ,but it is hidden
sheh.greet()


