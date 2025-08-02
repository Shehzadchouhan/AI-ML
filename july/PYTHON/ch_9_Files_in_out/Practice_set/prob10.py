with open("this.txt","w") as f:
    f.write("") # This line will raise an error because the file is opened in read mode.
    f.close()