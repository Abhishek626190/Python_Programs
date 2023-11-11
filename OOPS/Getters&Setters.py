class Student:
    schoolName="GyanGanga"
    def __init__():
        print("I am in default constructor")
    def __init__(self,id,name,age):
        print("I am in Parameterized Constructor")
        self.name=name
        self.age=age
        self.id=id
     
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
    def setId(self,i):
        self.id=i
    def getId(self):
        return self.id
    def setAge(self,a):
        self.age=a
    def getAge(self):
        return self.age
    
        
    def display(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("School Name:",self.schoolName)
obj=Student
obj1=Student(101,"Abhishek",22)
obj1.setName("Abhi")
s=obj1.getName()
#print(s)
obj1.display()
    
        