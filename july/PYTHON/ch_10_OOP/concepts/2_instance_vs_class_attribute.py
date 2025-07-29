# 2_instance_vs_class_attribute
class Employee:
    language="py" #This is a class attribute
    salary=120000

sheh=Employee()
sheh.language="js" # Note: Instance attributes, take preference over class attributes during assignment &
# retrieval
print(sheh.language,sheh.salary)


