#   map/reduce

#!/usr/bin/env python3
# -*- coding: utf-8 -
from functools import reduce
#1
def normalize(name):
    return name[0].upper()+name[1:].lower()

#测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#2
def prod(L):
    return reduce(lambda x,y:x*y,L)

print('\n3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#3
def str2float(L):
    s=L.find('.')
    return reduce(lambda x,y :x*10+y,map(int,L[:s]+L[s+1:]))/10**(len(L)-1-s)


print('\nstr2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')