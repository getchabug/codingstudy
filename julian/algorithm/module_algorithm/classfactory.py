class happy:
    def __init__(self):
        self.result = 0



    def plus(self, a, b):
        self.result = a+b
        return self.result


cal = happy()
print(cal.plus(3, 4))

