#-*- coding: utf-8 -*-
class coding:
    def __init__(self):
        self.result=0
    def sum(self,a,b):
        self.result=a**b
        print("%s**%s=%s입니다."%(a,b,self.result))
coding=coding()
print(coding.sum(5,9))