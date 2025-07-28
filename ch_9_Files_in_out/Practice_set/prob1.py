f=open("poem.txt","r")

content=f.read()
if("twinkle" in content):
    print("the word 'twinkle' is present")
else:
     print("the word 'twinkle' is not present")

f.close()