# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    # create an empty dictionary
    dict = {}
    # build a dictionary with the number as the key and the times it was counted as the value
    for num in arr:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    
    # when the dictionary has been built, we can simply return the key that has only been counted once
    for pair in dict:
        if dict.get(pair) == 1:
            return pair


print(find_uniq([ 0, 0, 0.55, 0, 0 ]))