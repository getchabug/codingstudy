

class test:
    def __init__(self):
        self.math=0
        self.googu=0
        self.science=0
        self.society=0
    def seahum(self,math,googu,science,society,):
        self.math=math
        self.googu=googu
        self.science=science
        self.society=society
        total=math+googu+science+society
        if total >200:
            s=("시험에 합격하셨습니다")
            return s
        elif total < 200:
            p=("시험에 낙제하였습니다")
            return p


result=test()
i=result.seahum(1,1,1,1)
print(i)

class aircorn:
    def __init__(self):
        self.cool=0
        self.cool_level=0
    def eurcorn(self,cool,cool_level):
        self.cool=cool
        self.cool_level=cool_level
        total=cool+cool_level
        return total

fey=aircorn()
g=fey.eurcorn(3,6)
print(g)








