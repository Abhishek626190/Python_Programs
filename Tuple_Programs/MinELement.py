t=(10,20,50,30,60)
print("The elements in list is: ",t)
min=t[0]
for i in range(len(t)):
    if(min>t[i]):
        min=t[i]
print("The minimum element in list is:",min)