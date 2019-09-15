

class delete:
    def __init__(self):
        self.X=0
        self.a=[]
    def dlt(self,X,a):
        self.X=X
        if X in a:
            a.remove(X)
            return a
        else:
            return a
fey=delete()
a=fey.dlt(3,[1,2,3,4,5])
print(a)




























