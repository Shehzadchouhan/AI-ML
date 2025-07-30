try:
   a=int(input("Enter your number:"))
   print("You entered:", a)
except Exception as e: 
   # it will throw an exception when you will not enetered any inrezer value
   # print("An error occurred:", e)
   print("Please enter a valid number.")