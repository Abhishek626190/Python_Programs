

l=[10,20,50,10,20,30,30,67,30]
print("before sorting")
print(l)
temp=0
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]<l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("After sorting")
print(l)