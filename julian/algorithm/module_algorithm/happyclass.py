class d:

    def __init__(self):
        self.result = 0


    def biggest(self, list1):
        list1.sort()
        return list1.pop()

cal = d()
print(cal.biggest(3))