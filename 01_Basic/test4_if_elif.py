#   条件判断

#   test4_if_elif.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = float(input('请输入您的身高（cm）\n...'))/100
weight = float(input('请输入您的体重（kg）\n...'))
bmi = weight/height**2
if bmi<18.5:
    b='过轻'
elif bmi<25:
    b='正常'
elif bmi<28:
    b='过重'
elif bmi<32:
    b='肥胖'
else:
    b='严重肥胖'
print('您的bmi指数为%.1f，体型属于%s'%(bmi,b))
