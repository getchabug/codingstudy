#-*- coding: utf-8 -*-
#수학 클래스 정의
class Math:
    #이 함수는 클래스 내에서 사용하는 변수 정의
    def __init__(self):
        self.result=0
    #param1,param2를 입력값으로 받아서, 더하기 연산을하고 self.result에 저장 한다음 return
    def add_2param(self,param1,param2):
        self.result=param1+param2

        return self.result
    #param1,param2를 입력값으로 받아서, 곱하기 연산을 하고 self.result에 저장 한다음 return
    def mul_2param(self,param1,param2):
        self.result=param1*param2

        return self.result
    #pram1,param2를 입력삾으로 받아서,나누기 연산을 하고 self.result에 저장 한다음 return
    def sub_2param(self,param1,param2):
        self.result=param1%param2

        return self.result
    #param1,param2를 입력값으로 받아서,빼기 연산을 하고 self.result에 저장 한다음 return
    def min_2param(self,param1,param2):
        self.result=param1-param2




        return self.resut







#param1,param2를 입력값으로 받아서,더하기 연산을 하고 self.result에 저장 한다음 return
    def sum_n(self,param1):
        for sum_target in range(1,param1+1):
            self.result= self.result

            return self.result
#param1,param2를 입력값으로 받아서,
    def mul_n(self,param1):
        for mul_target in range(1,param1*1):
            self.reslt=self.result

            return self.result

    def sub_n(self,param1):
        for sub_target in range(1,param%1):
            self.result=self.result

            return self.result
