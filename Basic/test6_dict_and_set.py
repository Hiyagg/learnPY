#   字典和集合

#   test6_dict_and_set
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

t1=(1,2,3)
t2=(1,[2,3])
try:
    d1={t1:t2}
    print('d1=',d1)
    d2={t2:t1}
    print('d2=',d2)
except TypeError as e:
    print('错误原因：%s\n' % e)
    #dict中key的对象必须是不可变的

try:
    s={t1,t2}
    print('s=',s)
except TypeError as e:
    print('错误原因：',e)

