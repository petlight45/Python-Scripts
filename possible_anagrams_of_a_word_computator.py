def anagram_finder(list_words):
    """
      This function computes and returns the possible anagrams of each word in a given list of words.

      Parameters:
      list_words(list): the list of words whose anagram is to be computed

      Return
      list: the computed anagrams as sublists
      """
    #Validation
    if type(list_words) != list:
        raise Exception("Invalid input; must be a list data type.")
    for item in list_words:
        if type(item) != str:
            raise Exception("Invalid Input: all items in the given list must be a string.")
    def permutation_loop(init_string, working_word):
        """
          This function is a function designed to be recursive for the purpose of computing the anagrams of a given word .
        """
        for letter in working_word:
            if letter in init_string:
                continue
            if len(init_string+letter) == len(working_word):
                if not (init_string+letter) in list_anagrams:
                    list_anagrams.append(init_string+letter)
            else:
                permutation_loop(init_string+letter, working_word)

    list_word_anagrams = []
    for word in list_words:
        list_anagrams = []
        permutation_loop("", word)
        list_word_anagrams.append(list_anagrams)
    text_format = "The anagrams of {0} are {1}."
    return text_format.format(list_words, list_word_anagrams)


print(anagram_finder(["bat", "hen", "fgh"]))