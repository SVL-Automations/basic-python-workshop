d={}
print(type(d))
student={'name':'abc','rollno':12,'marks':67.9}
print(student)
print(student['rollno'])

print(student.get('marks'))

for keys in student:
    print(student[keys])

print(student.keys())

print(student.values())


print(student.items())

for ele in student.items():
    print(ele[0],ele[1])

student['email']='abc@gmail.com'

print(student)

student.update({'age':23,'addr':'kolhapur'})
print(student)

student.update({'name':'shital'})
print(student)
print("Delete :")
student.pop('addr')
print(student)

student.popitem()
print(student)

del student['rollno']
print(student)
student.clear()
print(student)

del student
#print(student)

d={}

for i in range(1,16):
    d[i]=i**2

print(d)
import operator
d={12:34,90:56,23:78,4:25}
print("Sorted Dict")
sortd=sorted(d.items(),key=operator.itemgetter(0))
print(dict(sortd))
print(sorted(d.items(),key=operator.itemgetter(1)))