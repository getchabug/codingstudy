def lcm(a, b):
    if a > b:
        i = a
    else:
        i = b
    while True:
        if ((i % a == 0) and (i % b == 0)):
            lcm = i
            break
        i += 1
    return lcm


print(lcm(5, 13))