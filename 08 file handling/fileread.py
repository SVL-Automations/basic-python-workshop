
fp=open('hello.txt','r')


'''print(fp.read(10))
fp.seek(0)
print(fp.readline())
fp.seek(0)'''
print(fp.readlines())

fp.seek(0)

for line in fp.readlines():
    print(line,end='')
fp.close()

with open('hello.txt','a') as fp:
   # print(fp.read())
    fp.writelines(['efrergr\n','ergrtry\n','htrhyttyj\n'])
    fp.close()
