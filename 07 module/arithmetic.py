def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mult(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1/no2

def addlist(l):
    l2=l[::-1]
    l3=[]
    for i in range(len(l)):
        l3.append(l[i]+l2[i])
    return l3
import math
def mintime(N,v1,v2):
    t1=2*N/v2
    t2=math.sqrt(2)*N/v1
    if(t1<t2):
        print("Cab")
    else:
        print("Walk")
