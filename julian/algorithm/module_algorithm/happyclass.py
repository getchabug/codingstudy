class ddong:
    def __init__(self):
        self.result = 0


    def smallest(self, list1):
        list1.sort()
        return list1.pop(0)

cal = ddong()
print(cal.smallest(2))