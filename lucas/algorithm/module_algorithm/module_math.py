#--coding:utf-8--
from collections import Counter
a=[1,2,3,4,5]
class Math:
    def __init__(self):
        self.result=0

    def sum_n(self,param1):
    #param1을 입력값으로 받아서 1부터 param1까지 곱한다
        for sum_target in range(1, param1+1):
            self.result=self.result+sum_target
        return self.result

    #param1을 입력값으로 받아서 1부터 param1까지 더한다
    def mul_n(self,param1):
        for mul_target in range(1,param1+1):
            self.result=self.result*mul_target
        return self.result

    def biggest(self, list1):
        list1.sort
        return list1.pop()
    def smallest(self, list1):
        list1.sort()
        return list1.pop(0)
    def same_name(self,list1):
        test_dict = dict(Counter(["Tom", "Jerry", "MIke", "Tom"]))
        keys = list(test_dict.keys())
        values = list(test_dict.values())
        for value_idx, value_count in enumerate(values):
            if value_count > 1:
                return keys[value_idx]
    def different_name(self,list1):
        test_dict = dict(Counter(["Tom", "Jerry", "MIke", "Tom"]))
        keys = list(test_dict.keys())
        values = list(test_dict.values())
        for value_idx, value_count in enumerate(values):
            if value_count < 2:
                return keys[value_idx]
    def biggest(n):
        big = 0
        for i in a:
            if big < i:
                big=i
        return big
n=[100,2,3,4,5]



        # cal1=([1,2,3,4,5])
# class  cal1:
#     def sum(self, param11):
#         for i in self.param1:
#             total += i
#         return self.param1
#
#     def avg(self, param1):
#         for i in self.param1:
#             total+=i
#             total / len(self.param1)
#         return tatal
# print(cal1.sum())




a.sort