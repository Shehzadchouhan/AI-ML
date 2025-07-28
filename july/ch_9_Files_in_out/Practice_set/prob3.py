def generateTable(n):
  tables=""
  for i in range(1,11):
    tables+=f"{n} x {i} = {n*i}\n"

  with open(f"tables/table_{n}.txt","w") as f:
     f.write(tables)

for i in range(2,21):
    generateTable(i)