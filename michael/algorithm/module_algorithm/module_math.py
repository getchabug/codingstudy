#-- coding:utf-8--

#수학 클래스 정의
from collections import Counter
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
    def everyone(self,list3):
        test_dict=dict(Counter(['Tom','Jerry','Mike','Tom']))
        keys = list(test_dict.keys())
        values = list(test_dict.values())
        for value_idx, value_Count in enumerate(values):
            if value_Count > 1:
                return keys[value_idx]
    def every(self,list4):
        test_dicts=dict(Counter(['Tom','Jerry','Mike','Tom']))
        keys = list(test_dicts.keys())
        values = list(test_dicts.values())
        for value_idx, value_Count in enumerate(values):
            if value_Count < 2:
                return keys[value_idx]
    def biggest(n):
        big=0
        for i in n:
            if big < i:
                big=i
        return big
    n=[100,2,999,4,5,7]
    print(biggest(n))
    def gcd(a,b):
        i=min(a,b)
        while True:
            if a%i ==0and b%i==0:
                return i
            i=i-1
    print(gcd(1,5))
    print(gcd(3,6))
    print(gcd(60,24))
    print(gcd(81,27))
    def lcm(a,b):
        if a>b:
            i=a
        else:
            i=b
        while True:
            if((i%a==0)and(i%b==0)):
                lcm = i
                break
            i += 1
        return lcm
    print(lcm(5,13))

    def hanoi(list_a, list_b, list_c):
        count=0
        for element in list_a:
            i