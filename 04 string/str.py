str1="Python Programming"
str2="Programming"

str3=str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
#print(str3)

str3=str1[0]+str1[1:].replace(str1[0],'$')

print(str3)

def count(str1):
    up,lo,sp=0,0,0
    for l in str1:
        if l.isupper():
            up+=1
        if l.islower():
            lo+=1
        if l.isspace():
            sp+=1
    return up,lo,sp

u,l,sp=count(str1)
print("upper count {0} \n lower count {1} \nSpace count {2}".format(u,l,sp))