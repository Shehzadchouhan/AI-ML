import random
n=random.randint(1,100)
a=-1
guess=1
while(a!=n):
    a=int(input("Guess the number:"))
    if(a>n):
        print("Please lower number")
        guess+=1
    elif(a<n):
        print("please higher number")
        guess+=1
  
print(f"You guessed the correct number {n} in {guess} attempts")

