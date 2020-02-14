# A digital root is the recursive sum of all the digits in a number. 
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. This is only applicable to 
# the natural numbers.

def digital_root(num):
    # do an initial check to see if the number is already a single char
    if len(str(num)) == 1:
        return num
    # keep looping
    while True:
        # set up the sum counter
        sum = 0
        # for each number in the list of numbers add them together
        for number in str(num):
            sum = int(sum) + int(number)
        # if the sum is a singe number return it
        if len(str(sum)) == 1:
            return sum
        # otherwise set the result from previous additions to the num, to try it again
        else: 
            num = sum

print(digital_root(132189))