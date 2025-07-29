class Compony:
    a=1

class Employee(Compony):
    b=2

class coder(Employee):
    c=3

x=Compony()
print(x.a)
# print(x.b,x.c) #its give an error as b and c cant acces due to other class attributes

y=Employee()
print(y.a,y.b)
# print(x.c) ##its give an error as c cant acces due to other class attributes

z=coder()
print(z.a,z.b,z.c)
# print(x.c) ##its give an error as c cant acces due to other class attributes
