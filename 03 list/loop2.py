n=int(input("Enter number"))
f=0
sum=0
l=[12,45,67,93,97,43,111]
for ele in l:
    f=0
    for i in range(2,ele/2):
        if(ele%i==0):
            f=1
            #break
            continue
    
    if(f==0):
        sum=sum+ele

print("Sum",sum)