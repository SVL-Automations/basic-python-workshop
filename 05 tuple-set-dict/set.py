s=set()
s1={3,2,1,2,3,5,45,78,90}
print(s1)

s1.add(345)
s1.update([1,2,3,56,4,34])
print(s1)
s1.remove(34)
s1.discard(90)
print(s1)
#s1.remove(890)
s1.discard(1234)
print(s1.pop())

s1={12,3,4,5,78}
s2={2,5,9,65,17}

#s1.update(s2)
print(s1)

print(s1.intersection(s2))

#s2.intersection_update(s1)

print(s2)

print(s1.difference(s2))

#s1.difference_update(s2)

print(s1)
print(s1.symmetric_difference(s2))

s1.symmetric_difference_update(s2)

print(s1)

s1={1,2,3}
s2={1,2,3,4}

print(s1.issubset(s2))