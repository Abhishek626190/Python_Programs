t1=(10,20,50,30,40)
print("Before Sorting",t1)
size=len(t1)-1
temp=""
t=list(t1)
print(t,type(t))
for i in range(len(t)):
   if(size>i):
    temp=t[i]
    t[i]=t[size]
    t[size]=temp
    size=size-1
    
t2=tuple(t,)
print("After sort",t2,type(t2))
 