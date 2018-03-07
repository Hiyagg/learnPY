#   函数调用

#   test4_func_recur
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n,a,b,c):
    if n==1:
        print('%s --> %s'%(a,c))
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')