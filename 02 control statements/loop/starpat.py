'''
*
**
***
****
*****
'''

for i in range(1,6):
    for i in range(i):
        print('*', end=' ')
    print()
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''
for i in range(1,6):
    for sp in range(5-i):
        print(' ',end='')
    for j in range(1,i+1):
        print(j, end=' ')
    print()