class L:
    def __init__(self):
        self.result = 0

    def adder(self,num):
        self.result += num
        return self.result

L1 = L()
L2 = L()

print(L1.adder(7))
print(L2.adder(9))
