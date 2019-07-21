def blockchecker(list_a,list_b):
    global count
    list_b.append(list_a.pop())
    count = count + 1

a = [1, 2, 3]
b = []
c = []
count = 0
blockchecker(a,c)
blockchecker(a,b)
blockchecker(c,b)
blockchecker(a,c)
blockchecker(b,a)
blockchecker(b,c)
blockchecker(a,c)
print(count)