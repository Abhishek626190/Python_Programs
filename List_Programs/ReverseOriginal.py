
l=[10,30,67,60,70,50]
print('List BEfore Sorting')     
print(l)

temp=0
#count=1
size=len(l)-1
for i in range(len(l)):
    # temp=0
      if(size>i):
        temp=l[i]
        l[i]=l[size]
        l[size]=temp
        #count=count+1
        size=size-1
         
print('List After Sorting')     
print(l)
        
        