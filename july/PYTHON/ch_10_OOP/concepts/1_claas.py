class Employee:
    language="py" #This is a class attribute
    salary=120000

sheh=Employee()
sheh.name="karan" #this is an instance(object) attribute
print(sheh.name,sheh.language,sheh.salary)

anas=Employee()
anas.name="rohan"
print(anas.name,anas.salary,anas.language)

# here name is the instance(object) attribute and language , salary is class attribute 