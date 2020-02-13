def count_smileys(arr):
    # set up a counter
    count = 0
    # iterate through the array getting each face
    for thing in arr:
        length = len(thing)
        # if its a 2 char smiley check for valid chars
        if length == 2:
            if ';' in thing[0] or ':' in thing[0]:
                if ')' in thing[1] or 'D' in thing[1]:
                    # add to count if criteria matched
                    count = count + 1
        # if its a 3 char smiley check for valid chars
        if length == 3:
            if ';' in thing[0] or ':' in thing[0]:
                if '-' in thing[1] or '~' in thing[1]:
                    if ')' in thing[2] or 'D' in thing[2]:
                        # add to count if criteria matched
                        count = count + 1
    return count

print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))