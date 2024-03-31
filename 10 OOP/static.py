class Person:
    count=0
    def __init__(self,name,roll):
        self.name=name
        self._rollno=roll
        self.count+=1
    def display(self):
        print("Name is"+self.name+"\nId is:{0}".format(self._rollno))
    

class Student(Person):
   # count=0
    def __init__(self,name,roll,marks):
        super().__init__(name="abc",roll=34)
        self.marks=marks
        Person.count+=1
    @staticmethod
    def displaycount():
        print("No. of Students are {0}".format(Student.count))
        return
    
    counter=staticmethod(displaycount)

    def student_display(self):
        print("My name is "+self.name+"\nRoll no is {0}\nMarks are: {1}".format(self._rollno,self.marks))


s=Student("aaa",34,90)
s1=Student("saa",24,90)
s2=Student("caa",54,90)
s1.display()
s1.counter()
Student.counter()