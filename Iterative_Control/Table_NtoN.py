num=int(input("Enter starting number of table"))
num1=int(input("Enter ending number of table"))

while(num<=num1):
    i=1
    while(i<11):
        print(num,"*",i,"=",num*i)
        i=i+1
    print("******************")
    num=num+1
