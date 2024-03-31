n=int(input("Enter number"))

if n%2==0:
    if n in range(2,6):
        print("Not Wiered")
    elif n in range(6,21):
        print("Wiered")
    else:   
        print("Not Weired")
else:
    print("Weired")