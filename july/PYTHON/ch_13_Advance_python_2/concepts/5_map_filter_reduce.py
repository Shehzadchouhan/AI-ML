from functools import reduce # we need to imprt reduce function from functools
l=[1,2,3,4,5]

#Map example
square=lambda x:x*x

sqList=map(square,l)
print(list(sqList))

#Filter example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))

#Reduce example
def sum(a,b):
        return a+b
def mul(a,b):
        return a*b

print("sum : ",reduce(sum,l))
print("mul : ",reduce(mul,l))
