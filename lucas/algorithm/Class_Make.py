

class search:
    def __init__(self):
        self.X=0
        self.a=[]
    def research(self,X,a):
        self.X=X
        if X in a:
            r=X
            return r
        else:
            r=-1
            return r
fey=search()
a=fey.research(9,[1,2,3,4,5])
print(a)




























