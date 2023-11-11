class Person:
    
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display1(self):
        print("Name:",self.name," Age:",self.age)
obj=Person("Abhi",21)
obj.display1()

class Student(Person):
    pass
obj1=Student("Abhishek",22)
obj1.display1()