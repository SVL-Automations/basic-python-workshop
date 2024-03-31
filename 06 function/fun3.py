def sumofcubes(n):
    sum=0
    for i in range(n):
        sum+=i**3
    return sum

print(sumofcubes(5))

'''
123
3*10
2*10

1
'''
def intrev(n):
    num=0
    while(n>0):
        dig=n%10
        num=dig+num*10
        n=n//10
    return num

print(intrev(123))