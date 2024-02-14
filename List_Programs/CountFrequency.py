
l=[10,20,50,10,20,30,30,67,30]
count=0
max=0
ele=0
for  x in range(len(l)):
    count=0
    for y in range(len(l)):
        
        if(l[x]==l[y] and x>y):
            break
        elif(l[x]==l[y]):
            count=count+1
    if(count!=0):
        #print("Frequency of ",l[x],"=",count)
        if(count>max):
            max=count
            ele=l[x]
print("The Element whose frequency is Max is: element= ",ele,"and the frequency is =",max)