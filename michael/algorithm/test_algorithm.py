#-*- coding: utf-8 -*-
class coding:
    def __init__(self):
        self.result=0
    def sum(self,a,b,c,d,e,f,g):
        self.result=a+b-c*d/e**f/g
        return self.result
coding=coding()
print(coding.sum(7,1,6,2,5,3,4))