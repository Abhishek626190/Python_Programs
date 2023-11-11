sub1=int(input("Enter marks of 1st subject out of 100:"))
sub2=int(input("Enter marks of 2nd subject out of 100:"))
sub3=int(input("Enter marks of 3rd subject out of 100:"))
sub4=int(input("Enter marks of 4th subject out of 100:"))
sub5=int(input("Enter marks of 5th subject out of 100:"))
sum=sub1+sub2+sub3+sub4+sub5
per=sum/5

if(per>=95):
    print("A+ Grade")
elif(per>=90):
    print("A Grade")
elif(per>=80):
    print("B Grade")
elif(per>=70):
    print("C Grade")
elif(per>=60):
    print("D Grade")
else:
    print("You are fail")