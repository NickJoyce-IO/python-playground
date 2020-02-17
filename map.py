arr = [1,2,3,4,5,6,7]


def add1(num):
    return num + 1

new = map(add1, arr)

print(list(new))