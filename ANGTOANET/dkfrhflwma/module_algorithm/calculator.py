a=[1,3,4,2,5,6,7,8,9,10,100,12,13]
big=0
for i in a:
    small=i

    if big>small:
        continue

    elif big<=small:
        big=small
print (big)