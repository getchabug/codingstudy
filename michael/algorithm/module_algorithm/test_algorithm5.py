class coding:
    def __init__(self):
        self.result=0
    def cal(self,a,b,c,d,e):
        self.result=a**b+c-d*e
        return self.result
coding=coding()
print(coding.cal(7,2,9,5,4))