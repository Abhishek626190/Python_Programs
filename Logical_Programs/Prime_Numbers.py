num=int(input("Enter Number"))
count=0
i=2
while i<num:
    if num%i==0:
        count=count+1
        break
    i=i+1
if count==0:
    print("Prime number",num)
else:
    print("Not Prime Number",num)
    