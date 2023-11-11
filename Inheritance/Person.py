class Person:
    
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display1(self):
        print("Name:",self.name," Age:",self.age)
     
obj=Person("Abhishek",22)
#obj.display()

class Student(Person):
    def __init__(self,mn,oc):
        self.mobile=mn
        self.occupation=oc
        
        
        
    def display2(self):
        print("Mobile Number:",self.mobile,"Occupation:",self.occupation)
    
     
obj1=Student(6261904221,"Student")
obj2=Person("abhi",21)
obj2.display1()
obj1.display2()
 