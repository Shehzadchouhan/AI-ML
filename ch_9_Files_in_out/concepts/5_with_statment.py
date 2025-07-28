f=open("file.txt")
print(f.read())
f.close()

print("\n")

#thus same can be write using with statment like this
with open("file.txt") as f:
          print(f.read())
#we dont need to explicitly close the file