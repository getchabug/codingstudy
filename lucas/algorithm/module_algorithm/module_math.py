#--coding:utf-8--
n=[100,1000,2,3,4]
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
    def biggest(self,list1):
        big = 0
        for i in self.list1:
            if big < i:
                big=i
        return big
        print(biggest(n))
    def gcd(a, b):
        i=min(a,b)#i를 a와b중에 더 작은수로 입력한다
        while True:#무한반복한다
            if a % i ==0 and b % i ==0:#만약 a/b의 나머지가 0이고 b/i나머지도 0이면
                return i#i의값을 출력한다
            i = i-1#아니면 i에 1을 뺀다

    print(gcd(1,5))
    print(gcd(3,6))
    print(gcd(60,24))
    print(gcd(81,27))
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




a.sort