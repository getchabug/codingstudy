class A:
    def __init__(self):
        self.result = 0

    def adder(self,num,num1):
        self.result = num + num1
        return self.result

A = A()

print(A.adder(16,2))