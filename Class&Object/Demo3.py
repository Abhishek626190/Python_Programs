class A:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def __str__(self):
        return f"{self.n} {self.a}"
obj=A("Abhi",22)
print(obj)
 

class B:
    def __init__(self,id):
        self.id=id
 
    def __str__(self):
        return f"({self.id})"
    def m1(self):
        print("Hello")
    def m2(self,a,b):
         c=a*b
         print(c)
        
    
        
obj1=B(101)
print(obj1)
obj1.m1()
obj1.m2(10,5)

 


        