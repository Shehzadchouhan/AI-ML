class Employee:
    compony="tcs"
    name="sheh"
    def show(self):
        print(f"employee name is {self.name} and compony is {self.compony}")

class coder:
    language="python"
    def printLanguage(self):
        print(f"Out of all the language ,your favorite language is {self.language}")

class programmer(Employee,coder):
    compony="Itc"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language}")
    
a=Employee()
b=programmer()

# b is the derived class of both employee and coder
b.show() #method of class employee
b.printLanguage() #method of class coder
b.showLanguage() #method of class programmer