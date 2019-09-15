class C:
    def __init__ (self):
        self.result = 0

    def adder(self,num,num1):
        self.result = num + num1
        return self.result

C = C()

print(C.adder(147683635,182748586937))