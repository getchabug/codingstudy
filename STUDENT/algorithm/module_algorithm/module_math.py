#-- coding:utf-8--

#수학 클래스 정의
class Math:

    #클래스 내에서 공통으로 사용하는 변수 정의
    def __init__(self):
        self.result = 0
    #param = pramameter,변수 (예; 1+2에서 1과2
    #param1,param2를 입력값으로 받아서,
    #더하기 연산을 하고self.result에 저장한다음 return
    def add_2param(self,param1,param2):
        self.result = param1 + param2

        return self.result
    #param1,param2를 입력값으로 받아서,
    #곱하기 연산을 하고self.result에 저장한다음 return
    def mul_2param(self,param1,param2):
        self.result=param1*param2

        return self.result
    #param1,param2를 입력값으로 받아서,나누기 연산을 하고self.result에 저장한다음 return
    def sub_2param(self,param1,param2):
        self.result=param1/param2


        return self.result
    #param1,param2를 입력값으로 받아서,빼기 연산을 하고self.result에 저장한다음 return
    def divide_2param(self,param1,param2):
        self.result=param1-param2
        return self.result