def anagrams(word, words):
    # create array to store matches
    arr = []
    # sort the word as we can compare this with words
    sortedWord = sorted(word)
    # get the length of the word to use as a comparison
    wordcount = len(word)
    # loop through the words array
    for text in words:
        # only do this for words of the same length
        if len(text) == wordcount:
            # if the sorted word matches the sorted word from the array add it to the new array
            if sorted(text) == sortedWord:
                arr.append(text)
    return arr
print(anagrams('racer',['crazer', 'carer', 'racar', 'caers', 'racer']))

#print(sorted('racer'))
#print(sorted('carer'))
