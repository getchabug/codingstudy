class Calculator:
    def __init__(self, input_list):
        self.sum=0
        self.list= input_list
    def sum_(self):
        for i in self.list:
             self.sum += i
        return self.sum
    def avg(self):
        result_sum = self.sum_()
        a = result_sum/len(self.list)
        return a
cal1=Calculator([1,2,3,4,5])
print(cal1.sum_())
print(cal1.avg())
cal2=Calculator([6,7,8,9,10])
print(cal2.sum_())
print(cal2.avg())
a=60
b=25
if a<b:
    i=a
elif a>b:
    i=b

while a%i < 1:
    i-1










