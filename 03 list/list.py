l1=[]
l2=[1,3,4,5,'abc',[6,78],('err',67),1,2]

print(l1)
print(type(l2))

print(l2[4])
#l2[4]=3+9j
print(l2)

print(l2[:4])

print(l2[5:])

print(l2[3:7])

print(l2[::2])

print(l2[-4:-1])

l1.append(12)
print(l1)

l1.append('asdfg')
print(l1)

l1.insert(1,45)

print(l1)

l1.insert(3,[1,2,3])
print(l1[3][1])

l1.extend([1,2,3,4])
print(l1)

l1.pop()
print(l1)

l1.pop(4)
print(l1)

l1.remove([1,2,3])
print(l1)

del l1[2]
print(l1)

#del l1
l1.clear()
print(l1)

l3=[34,56,12,3,89,12,78,1,29]

print(l3.index(12))
l3.sort(reverse=True)
print(l3)

print(l3.index(12))

print(l3.count(12))

l4=l3.copy()
print(l4)

print(len(l3))

print(sum(l3))
print(min(l3))
print(max(l3))

'''no=input("Enter number")
l=[]
for i in no:
   l.append(int(i))

print(l) 
'''
l=[0,1,153,370,371,407,657,34,90,12,356]
armsum=0
for no in l:
   sum=0
   n1=no
   while no>0:
      rem=no%10
      no=no//10
      sum=sum+rem**3
      #print(sum)
   if sum==n1:
      print(n1,end=' ')
      armsum+=n1

print(armsum)

l=[1,2,3,4,5]

k=int(input("Enter no of rotations"))

for i in range(k):
   x=l.pop()
   l.insert(0,x)

print(l)