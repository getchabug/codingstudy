a=[100,2,3,4,5,7]
big=0
for i in a:
    small=i
    if big>small:continue
    elif big<=small:
        big=small
print(big)
