l=[3,234,43,12]
index=0

# for item in l:
#     print(f"the item number at {index} is {item}")
#     index+=1

# Using enumerate to achieve the same result
for index,item in enumerate(l):
    print(f"the item number at {index} is {item}")