n1,n2,n3=90,45,12

if n1>n2 and n1>n3:
    print("{0} is greater".format(n1))
elif n2>n1 and n2>n3:
    print("{0} is greater".format(n2))
else: 
    print("{0} is greater".format(n3))

year=int(input("Enter year"))

if(year%400==0):
    print("leap year")
elif year%100 ==0:
    print("not leap year")
elif year%4==0:
    print("leap year")
else:
    print("not a leap year")