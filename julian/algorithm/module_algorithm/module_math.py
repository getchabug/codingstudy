#-*- coding: utf-8 -*-

#수학 클래스 정의
class Math:


    #클래스 내에서 공통으로 사용하는 변수 정의
    def __init__(self):
        self.result = 0

    #param1, param2를 입력값으로 받아서, 더하기 연산을 하고
    #self.result에 저장한다음 return
    def add_2param(self, param1, param2):
        self.result = param1 + param2
        return self.result

    #param1,param2를 입력값으로 받아서, 곱하기 연산을 하고
    #self.result에 저장한다음 return
    def mul_2param(self, param1, param2):
    #param1,param2를 입력값으로 받아서, 빼기연산을 하고
    #self.result에 저장한다음 return
        self.result = param1 * param2
        return self.result

    def sub_2param(self, param1,param2):
        self.result = param1 - param2
        return self.result

    #param1,param2를 입력값으로 받아서, 나누기연산을 하고
    #self.reult에 저장한다음 return
    def min_2param(self,param1, param2):
        self.result = param1 / param2
        return self.result


    def sum_n(self, param1):#param1 = 10

        for sum_target in range(1, param1 + 1):
            self.result = self.result + sum_target

        return self.result

    #param1 = 10 1부터그리고 제시한 숫자
    def mul_n(self, param1):#param1을 입력값으ㅡ로 받고 곱하기를 한다
        print("hello")
        for sum_target in range(1, param1 * 1):#그래서 1부터 param1을 곱한더
            self.result = self.result * sum_target
        return self.result

    def biggest(self, list1):
        list1.sort()
        return list1.pop()


    def smallest(self, list1):
        list1.sort()
        return list1.pop(0)






