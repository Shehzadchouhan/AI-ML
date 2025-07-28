f=open("file.txt","r")

#print all lines at once
# lines=f.readlines()
# print(lines,type(lines))


# print line by line one by one
# line1=f.readline()
# print(line1,type(line1))
# line2=f.readline()
# print(line2,type(line1))
# line3=f.readline()
# print(line3,type(line1))
# line4=f.readline()
# print(line4,type(line1))
# line5=f.readline()
# print((line5==""),type(line5))


#print lines using while loop
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
# f.close()