def blockchecker(list_a,list_b,count):
    global count
    list_b.appened(list_a.pop())
    count=count+1

a=[1,2,3]
b=[]
c=[]
count=0
blockchecker(a,c)
blockchecker(a,b)
blockchecker(c,b)
blockchecher(a,c)
blockchcker(b,c)
blockchcker(a,c)
print(count)