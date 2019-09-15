class coding:
    def __init__(self):
        self.result=0
    def sum(self,a,b,c,d):
        self.result=a**b+c-d
        return self.result
coding=coding()
print(coding.sum(5,3,9,12))