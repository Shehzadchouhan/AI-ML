a=int(input("Enter your number 'a':"))
b=int(input("Enter your number 'b':"))

if(b==0):
    raise ZeroDivisionError("You cannot divide by zero.")
# This code will raise an exception if the user inputs a b=0 value
else:
    print(f"The division of a and b is: {a/b}")