# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})

def count(string):
    # initialise dictionary
    dict = {}
    # loop through each letter in the string
    for letter in string:
        # if the letter isnt in the dict add it it as key and 1 as value
        if letter not in dict:
            dict[letter] = 1
        # else if it does already exist increment by 1
        else:
            dict[letter] = dict[letter] + 1
    return dict