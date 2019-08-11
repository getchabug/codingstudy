class B:
    def __init__(self):
        self.result = 0

    def adder(self,num,num1):
        self.result = num + num1
        return self.result

B = B()

print(B.adder(99,999))