t=(10,20,30,40,50,50)#tuple is ordered collection and it can store duplicate element
t1=(10,"Abhi",10.25,True)#tuple is heterogenous i.e we can store any type of element
print(t1[0])#tuple is indexed based i.e. we can access via index
print(t)
print(type(t))
print(t1)
print(type(t1))
#t1[6]=25#tuple is immutable i.e. we can not add or delete element in tuple once we declare
#del(t[0])#immutable
t2=(5)#this is not a tuple this is simply int if only one value then , is mandatory
print(t2)
print(type(t2))
t3=(5,)
print(t3)
print(type(t3))
t4=tuple((5,))#tuple costructor
print(t4)
print(type(t4))
t5=()#empty tuple
print(t5,type(t5))
