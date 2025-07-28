def factorial(n):
    if(n==0 or n==1):
       return 1
    else:
       return n*factorial(n-1)

n=int(input("Enter your number:"))
fact=factorial(n)
print(f"factorial of your number is {fact}")