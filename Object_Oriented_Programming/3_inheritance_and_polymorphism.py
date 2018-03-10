# 继承和多态

#!/usr/bin/env python3
# -*- coding: utf-8 -

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
    def run(self):
        print('Student is running')


class Boy(Student):
    def __init__(self, name, gender,love):
        Student.__init__(self,name,gender)
        self.love = love
    def get_gender(self):
        return self._Student__gender+' M'

class Girl(Student):
    def get_gender(self):
        return self._Student__gender + ' F'
    def run(self):
        print('Girl is running')
class Cat(object):
    def run(self):
        print('mmmmm')

def run2(student):
    student.run()
    student.run()

A=Student('Jobs','Male')
B=Boy('Jack','Male','Foorball')
C=Girl('Jane','Famale')
D=Cat()
print(A.name,A.get_gender(),'\n',
B.name,B.get_gender(),B.love,'\n',
C.name,C.get_gender())
B.set_gender('Female')
print(B.get_gender())
run2(A)
run2(C)
run2(D)



