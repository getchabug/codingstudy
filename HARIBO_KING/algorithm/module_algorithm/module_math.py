#-- coding: utf-8 --

#수학 클래스 정의
from collections import Counter
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
        self.result = param1 * param2
        return self.result

    #param1,param2를 입력값으로 받아서, 빼기연산을 하고
    #self.result에 저장한다음 return
    def sub_2param(self, param1,param2):
        self.result = param1 - param2
        return self.result

    #param1,param2를 입력값으로 받아서, 나누기연산을 하고
    #self.reult에 저장한다음 return
    def min_2param(self,param1, param2):
        self.result = param1 / param2
        return self.result

    def sum_n(self,param1):

        for sum_target in range(1,param1+1):
            self.result = self.result + sum_target

        return self.result
    #param1을 입력값으로 받아서, 곱하기를 하고
    def mul_n(self,param1):

        for mul_target in range(1,param1*1):
            self.result = self.result * mul_target

        return self.result


    def biggest(self,list1):
        list1.sort()
        return list1.pop()

    def smallest(self,list1):
        list1.sort()
        return list1.pop(0)

    def everyone(self,list1):
        test_dict = dict(Counter(["Tom", "Jerry", "Mike", "Tom"]))
        keys = list(test_dict.keys())
        values = list(test_dict.values())
        for value_idx, value_count in enumerate(values):
            if value_count > 1:
                return keys[value_idx]

    def every(self, list2):
        test_dicts =dict(Counter(["Tom", "Jerry", "Mike", "Tom"]))
        keys = list(test_dicts.keys())
        values = list(test_dicts.values())
        for value_idx, value_Count in enumerate(values):
            if value_Count < 2:
                return keys[value_idx]

    def getMax(n):
        max =
        for i in n:
            if max < i:
                max = i
        return max
    n = [1,100,300,2,99999,3,4]

    print(getMax)


