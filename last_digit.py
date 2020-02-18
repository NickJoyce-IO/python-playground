def last_digit(x,y):
    sum = x
    for i in range(y-1):
        sum *= x
    res = str(sum)
    return res[-1]



# print(last_digit(9,7))

print(last_digit(3,10))


