try:
    a=int(input("Enter your number: "))
    print(a)
except Exception as e:
    print("An error occurred:", e)
else:
    print("i am inside else block")