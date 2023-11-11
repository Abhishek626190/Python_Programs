num=int(input("Enter number"))
sum=0
while num!=0:
    rem=num%10
    if rem%2!=0:
        sum=sum+rem
    num=num//10
print(sum)