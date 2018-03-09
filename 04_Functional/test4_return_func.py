#   return_func

#!/usr/bin/env python3
# -*- coding: utf-8 -

def createCounter():
    n=[0]
    def counter():
        n[0]+=1
        return n[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
