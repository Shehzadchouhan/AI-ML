def greater(a,b,c):
    if(a>b and a>c):
        print(f"Greatest is a={a}") 
    
    if(b>a and b>c):
        print(f"Greatest is b={b}") 
    
    if(c>a and c>b):
        print(f"Greatest is c={c}") 

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
greater(a, b, c)