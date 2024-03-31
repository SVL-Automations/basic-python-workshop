
fp1=open("hello.txt",'r')
fp2=open("test.txt",'a+')

#data=fp1.read()

fp2.write(fp1.read())
fp2.seek(0)

for line in fp2.readlines():
    print(line)


fp1.close()
fp2.close()