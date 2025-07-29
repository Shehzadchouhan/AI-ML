std1=int(input("Enter your marks in sub1:"))
std2=int(input("Enter your marks in sub2:"))
std3=int(input("Enter your marks in sub3:"))

#check for total percentage
total_percentage=((std1+std2+std3)*100)/300 

if(std1>=33 and std2>=33 and std3 >= 33 and total_percentage>=40):
        print("student is passed,total percentage:",total_percentage)

else:
    print("student is failed,total percentage:",total_percentage) 
    