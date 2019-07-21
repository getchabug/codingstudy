a = [1,2,3]
b = []
c = []
count = 0

def blockchecker(list_a,list_b, count):
    list_b.append(list_a.pop())
    count = count + 1
