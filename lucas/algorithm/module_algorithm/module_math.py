#--coding:utf-8--
class Math:
    def __init__(self):
        self.result=0

    def sum_n(self,param1):
    #param1을 입력값으로 받아서 1부터 param1까지 곱한다
        for sum_target in range(1,param1+1):
            self.result=self.result+sum_target
        return self.result
    #param1을 입력값으로 받아서 1부터 param1까지 더한다
    def mul_n(self,param1):
        for mul_target in range(1,param1+1):
            self.result=self.result*mul_target
        return self.result
    def biggest(self, list1):
        list1.sort()
        return list1.pop()