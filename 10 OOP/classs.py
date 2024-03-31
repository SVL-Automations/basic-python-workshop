class Person:
    def __init__(self,name,roll):
        self.name=name
        self._rollno=roll
       # self._marks=70
    def display(self):
        print("Name is"+self.name+"\nId is:{0}".format(self._rollno))
    

class Student(Person):
    def __init__(self,name,roll,marks):
        super().__init__(name="abc",roll=34)
        self.marks=marks


    def student_display(self):
        print("My name is "+self.name+"\nRoll no is {0}\nMarks are: {1}".format(self._rollno,self.marks))
    
    
    
    
St=Student("shital",12,90)
St.student_display()
St.display()
