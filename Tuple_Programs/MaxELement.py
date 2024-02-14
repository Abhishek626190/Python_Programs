t=(10,20,50,30,60)
max=0
print("Tuple Elements")
print(t)
for i in range(len(t)):
    if(t[i]>max):
        max=t[i]

print("The maximum elements in tuple is:",max)