# 枚举类

# !/usr/bin/env python3
# -*- coding: utf-8 -

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')