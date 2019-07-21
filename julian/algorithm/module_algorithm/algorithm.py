def blockchecker(list_a, list_b):
    global count
    list_b.append(list_a.pop())
    count = count + 1
a=[1,2,3]
b=[]
c=[]
count = 0
blockchecker(a, c, count)

blockchecker(a, b, count)

blockchecker(c, b, count)

blockchecker(a, c, count)

blockchecker(a, b, count)

blockchecker(b, c, count)

blockchecker(a, c, count)

print(count)




