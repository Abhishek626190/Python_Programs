class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def display(self):
        print(self.firstname,self.lastname)
obj=Person("Abhishek","Rai")
obj.display()

class Student(Person):
    def __init__(self,fname,lname,age,gender):
        super().__init__(fname,lname)
        self.age=age
        self.gender=gender
    def display(self):
        return super().display(),print(self.age,self.gender)
obj1=Student("Abhishek","Rai",21,"Male")
obj1.display()
    