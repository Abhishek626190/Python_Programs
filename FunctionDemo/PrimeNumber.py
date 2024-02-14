def check(num):
    isPrime=False
    for i in range(2,num):
        if(num%i==0):
            isPrime=True
    return isPrime
num=int(input("Enter Number"))
res=check(num)
if(res==False):
    print(num," is Prime Numer")
else:
    print(num," is NOT Prime Number")