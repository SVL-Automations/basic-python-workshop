def add(no1,no2=56):
    return no1+no2

print(add(890,1234))
print(add(890))

def printvalues(rollno, name, marks):
    print("Roll no:",rollno)
    print("name:",name)
    print("marks:",marks)


printvalues(name="abc",rollno=23,marks=89.65)

printvalues(90,'hgfjhh',78.98)

def printnames(*name):
    for n in name:
        print(n)

printnames('abc','ahjg','uiyu','yugyg')

def printname(**name):
    print("First name: ",name['fname'])
    print(name['mname'])
    print(name['lname'])

printname(fname='abc',mname='ahjg',lname='uiyu')