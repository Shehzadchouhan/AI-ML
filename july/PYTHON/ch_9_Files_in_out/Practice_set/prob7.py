with open("logfile.txt") as f:
    lines=f.readlines()

lineno=1
for line in lines:
        if ("python" in line):
            print(f"it is found in line no.{lineno}")
            break
        lineno+=1
else:
        print("word not found in the file.")
        f.close()