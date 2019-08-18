class S:
    def __init__(self):
        self.result = 0



    def sum_n(self, a):

        for sum_target in range(1, a + 1):
            self.result = self.result + sum_target

        return self.result


cal = S()
print(cal.sum_n(6))

