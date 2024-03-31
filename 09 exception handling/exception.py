no1=234
no2=56
str="asbdf"
try:
    result=no1/no2
    print(result)
    print(str[7])
except ZeroDivisionError:
    print("Divide by Zero")
except IndexError:
    print("out of bound index")
else:
    print("Error")
finally:
    print("Finally block")

