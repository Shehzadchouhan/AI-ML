# Airthmatic opt
a=3
b=4
c=a+b
print(c)

#Assignment opt
a=4-8
print(a) #-4
b=5
b+=3 #increment and then assign value to b 8
b-=4 #decrement and then assign value to b 4
print(b)

#comparison opt
d= 5>=5
print(d)

#Logical opt
print("Truth Table for OR, AND, NOT")
print("\nA B  A|B  A&B  not A")
for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, "  ", A|B, "   ", A&B, "   ", int(not A))
