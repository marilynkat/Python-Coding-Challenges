def anagram(word1, word2):
    #Change words to lowercase to get format the same
    word1 = word1.lower()
    word2 = word2.lower()

    #Sort words in alphabetical order
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    #Return boolean to indicate whether anagram or not
    return sorted_word1 == sorted_word2

#Call function and print results
print("Is it an anagram? - ", anagram("save", "vase"))
print("Is it an anagram? - ", anagram("cookie", "cook"))