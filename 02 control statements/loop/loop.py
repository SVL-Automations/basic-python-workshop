str="python programming1"

v=0
c=0
for char in str:
    if char in 'aeiou':
        v=v+1
    else:
        c=c+1

print("vowel:", v)
print("Consonant: ", c)
l1=[12,45,34,78,56,23,69]
e=0
o=0
for no in l1:
    if(no%2)==0:
        e=e+1
    else:
        o=o+1

print("Even:", e)
print("Odd: ", o)

for i in range(1,len(str),2):
    #if i%2==0:
    print(str[i],end='')
print()
sum=0
for n in range(1,100,2):
    sum=sum+n

print("Sum of odd nos : ",sum)



    