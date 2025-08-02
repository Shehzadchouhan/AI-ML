with open("this.txt") as f:
    contnet=f.read()

with open("this_copy.txt","w")as f:
    f.write(contnet)
    f.close()