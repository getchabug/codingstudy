class happy:
    def __init__(self):
        self.result = 0



    def divide(self, a, b):
        self.result = a/b
        return self.result


cal = happy()
print(cal.divide(3, 4))

