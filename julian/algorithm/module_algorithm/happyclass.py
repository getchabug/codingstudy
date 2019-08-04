class p:
    def __init__(self):
        self.result = 0

    def begi(self, a, b):
        self.result = a - b
        return self.result


cal = p()
print(cal.begi(4, 6))