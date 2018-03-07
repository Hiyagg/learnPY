#   函数定义

#   test2_func_def
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def quadratic(a,b,c):
    dt=b**2-4*a*c
    if dt<0:
        print('此方程无实根')
        return
    else:
        return ((-b+dt**0.5)/2/a,(-b-dt**0.5)/2/a)

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')