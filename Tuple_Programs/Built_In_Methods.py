t1=(10,"Abhi",10.56,True)
t2=(10,50,4)
t1=t1+t2#concatenation of tuple
print(t1)
t3=(t1,t2)#nesting of tuple
print(t3)
t4=("Abhi",)*4#repetition
t5=(10,)*5#repetition
print(t4,type(t4))
print(t5,type(t5))
# t6=t1[1:len(t1)]#slicing
t6=t1[1:-1]#slicing
print(t6,type(t6))
# del(t6)
print(t6)