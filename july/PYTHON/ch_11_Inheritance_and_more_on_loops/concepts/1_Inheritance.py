class Employee:  #Parent class
    compony = "ITC"
    name="shehad" 
    salary=213
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     compony="Infoysis"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")
#     def showLanguage(self):
#         print(f"the name of the employee is {self.name} and this language is {self.showLanguage}")

class Programmer(Employee):  # Derived class
    compony="Infoysis"
    def showLanguage(self):
        print(f"the name of the employee is {self.name} and this language is {self.showLanguage}")

b=Programmer()
print(b.compony,b.show())




    
