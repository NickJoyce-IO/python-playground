def last_digit(x,y):
    sum = x
    for i in range(y-1):
        sum *= x
    res = str(sum)
    return res[-1]



# print(last_digit(9,7))

print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651))

