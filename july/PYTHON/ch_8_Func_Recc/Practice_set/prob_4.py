# sum of n natural numbers using recursion

def sum_natural(n):
 if (n==1):
  return 1
 else:
  return n + sum_natural(n-1)
 
n=int(input("Enter a natural number: "))
natural=sum_natural(n)
print(f"Sum of first {n} natural numbers is:", natural)