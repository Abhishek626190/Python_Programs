l1=[50,100,40,60,70]
print(l1[-1])#negative indexing
print(l1[-2])
print(l1[-3])

#*************************
#delete list element
del l1[0]
print(l1)
del l1[-1]
print(l1)
#*************************
#edit list element
l1[1]=200
l1[2]=500
print(l1)
#**********************
# add element list
#l1[3]=100  #error IndexError: list assignment index out of range
# by using append(value) method add element it add in last 
l1.append(300)
print(l1)
#insert (index,value)
l1.insert(1,400)
print(l1)

l1.insert(-6,700)
print(l1)

print(len(l1))
 

