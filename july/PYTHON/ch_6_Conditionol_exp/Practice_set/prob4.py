username=input("Enter your username:")

length=len(username)
print(length)
if(length<10):
    print("username contains less than 10 characters")
else:
    print("username not contains less than 10 characters")