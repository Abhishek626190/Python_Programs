class Student:
    schoolName="GyanGanga"
    def __init__(self):
        print("I am in default constructor")
    # def __init__(self,id,name,age):
    #     print("I am in Parameterized Constructor")
    #     self.name=name
    #     self.age=age
    #     self.id=id
     
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
#n=int(input("Enter Number Of Students"))
slist=[]
while True:
    #for i in range(n):
    s=Student()
    name=input("Enter Student Name")
    id=int(input("Enter student id"))
    age=int(input("Enter Student Age"))
    s.setName(name)
    s.setAge(age)
    s.setId(id)
    slist.append(s)
    y=input("Enter Yes for continue")
    if(y.lower()!="yes"):
        break
            
      
for e in slist:
    print("Student Id",e.getId())
    print("Student Name",e.getName())
    print("Student Age",e.getAge())
    print("School Name:",Student.schoolName)

    print()
        
# obj=Student
# obj1=Student(101,"Abhishek",22)
# obj1.setName("Abhi")
# s=obj1.getName()
# #print(s)
# obj1.display()
    
        