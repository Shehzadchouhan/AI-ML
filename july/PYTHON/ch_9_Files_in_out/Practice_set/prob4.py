word = "donkey"

with open("output.txt","r") as f:
    content=f.read()

contentNew=content.replace(word, "######")

with open("output.txt", "w") as f:
    f.write(contentNew)
    f.close()