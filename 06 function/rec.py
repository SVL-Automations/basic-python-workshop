count=10
def printhello(count):

    if(count>0):
        print("Hello")
        printhello(count-1)

printhello(10)

'''
2^4
2*2*2*2

1*2
2*2
4*2
8*2
'''

def power(num,pow):
    if(pow==1):
        return num
    else:
        return num*power(num,pow-1)
    
print(power(2,4))


        