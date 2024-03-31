class Employee:
    def __init__(self,id,name, salary, dept):
        self.id=id
        self.name=name
        self.salary=salary
        self.dept=dept

    def display_details(self):
        print("Id: ",self.id)
        print("Name: ",self.name)
        print("Salary: ",self.salary)
        print("Department: ",self.dept)
    
    def assign_dept(self, dept):
        self.dept=dept

    def calculatesalary(self,hrs):
        amount=0
        if(hrs>50):
            h=hrs-50
            self.amount=h*(self.salary/50)
        print("Total Salary: ",self.salary+self.amount)


e1=Employee("aaa",34,56789,"CSE")
e2=Employee("sss",23,34567,"Accounts")
e3=Employee("hgjh",78,67890,"Establishment")
e4=Employee("hgh",12,23456,"Exam")

e1.display_details()
e2.display_details()
e3.assign_dept("Mech")
e3.display_details()
e4.calculatesalary(80)
