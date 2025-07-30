mylist=[1,2,3,4,5]

squareList=[]
for item in mylist:
    squareList.append(item**2) # or item *item
print(squareList)


# using list comprehension
squareList = [i*i for i in mylist]
print(squareList)