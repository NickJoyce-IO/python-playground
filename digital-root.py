def digital_root(num):
    if len(str(num)) == 1:
        return num
        break
    else:
        sum = 0
        num = str(num)
        for number in num:
            sum = int(sum) + int(number)
        digital_root(sum)
        
print(digital_root(493193))