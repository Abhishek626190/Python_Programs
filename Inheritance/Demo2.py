class Employee:
    def __init__(self,name,id)  :
        self.id=id
        self.name=name
    def printname(self):
        print("Name:",self.name,"Id:",self.id)


class Manager(Employee):
    def __init__(self,name,id,role,salary):
        super().__init__(name,id)
        self.role=role
        self.salary=salary
    def display(self):
        return super().printname(),print("Role:",self.role,"Salary:Rs:",self.salary)
obj=Manager("Abhishek",101,"Developer",60000)
obj.display()