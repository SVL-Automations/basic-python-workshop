l=[1,2,3,4,5]

def addition(l):
    sum=0
    mult=1
    for e in l:
        sum+= e
        mult*=e
    return sum,mult

sum,mult=addition(l)
print("Sum is: {0} Mult is :{1}".format(sum,mult))
