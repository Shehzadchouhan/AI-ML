def multiplication_table(n):
   if(n==0):
      return
   else:
     for i in range(1, 11):
      print(f"{n} X {i} = {n * i}")
   

n=int(input("Enter a number to print its multiplication table: "))
multiplication_table(n)