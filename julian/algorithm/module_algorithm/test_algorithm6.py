f=1
for i in range(1,7+1):
    f=f+i
print(f)



A = [1,2,9999,4,5]


big = 0
for i in A:
    small = i


    if big > small:
        continue



    elif big <= small:
        big = small


        print(big)
