a=[1,2,3]
b=[]
c=[]
count=0
if len(a)<3:
    count+1
print(count)
def blockchecker(list_a,list_b,count):
    list_b.append(list_a.pop())
    count=count+1