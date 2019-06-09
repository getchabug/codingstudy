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
        self.result=param%param2

        return self.result
    #param1,param2를 입력값으로 받아서,빼기 연산을 하고self.result에 저장한다음 return
    def divide_2param(self,param1,param2):
        self.result=param1-param2
        return self.result
    #param1을 입력값으로 받아서,1부터 param1 까지 다 더한다.
    def sum_n(self, param1):

        for sum_target in range(1, param1+1):
            self.result = self.result + sum_target
        return self.result
    #param1을 입력값으로 받아서,1부터 param1 까지 곱한다.
    def mul_n(self, param1):

        for mul_target in range(1,param1+1):
            self.result = self.result * mul_target
        return self.result

    def biggest(self,list1):
        list1.sort()
        return list1.pop()

    def smallest(self,list2):
        list2.sort()
        return list2.pop(0)

