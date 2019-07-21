a=[3,2,1]
b=[]
c=[]
count = 0

def blockchecker(list_a,list_b,count):
    list_b.append(list_a.pop())
    count=count+1

blockchecker(a,c,count)
blockchecker(a,b,count)
blockchecker(a,c,count)
a.pop()
b.insert(0,2)
count=(count+1)
c.pop()
b.insert(1,1)
count=(count+1)
a.pop()
c.insert(0,3)
count=(count+1)
b.pop()
a.insert(0,1)
count=(count+1)
b.pop()
c.insert(1,2)
count=(count+1)
a.pop()
c.insert(2,1)
count=(count+1)
print(count)