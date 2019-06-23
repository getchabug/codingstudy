A = [1,100, 300, 2, 99999, 3,4]

big = 0
for i in A:
    small = i

    if big > small:
        continue

    elif big <= small:
        big = small

print(big)
