num=int(input("Enter number to reverse "))
temp=num
reverse1=0
sum=0
while num>0:
    rem=num%10
    reverse1=reverse1*10+rem
    num=num//10
print("The Reverse of the ",temp,"is :",reverse1)
#print(num)
# (/) operator always gives result in float