num=int(input('Enter number '))
mul=1
while num>0:
    rem=num%10
    mul=mul*rem
    num=num//10
print(mul)
