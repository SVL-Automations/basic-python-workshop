fp1=open("hello1.txt",'r')
fp2=open("test.txt",'w')

for line in fp1.readlines():
    if line.startswith('#'):
        pass
    else:
        fp2.write(line)
fp2.close()
fp1.close()