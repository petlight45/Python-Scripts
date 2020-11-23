def hangman(word, trials):
    """
    This function initializes a game of hangman.

    Parameters:
    word (str): The word that is to be guessed.
    trials (int): the no of times you are permitted to guess the wrong letter

    Return
    None
    """
    #Validation codes
    if not type(word)==str:
        print("Invalid input(s); word must be a string")
        return
    try:
        trials = int(trials)
    except:
        print("Invalid input(s); trials must be an integer")
        return

    def format_output_string():
        formatted_string = ""
        count_dict = {}
        for char in word.lower():
            index = count_dict.get(char, 0)
            if dict_word_booleans[char][index]:
                formatted_string += char
            else:
                formatted_string += "_"
            count_dict[char] = count_dict.get(char, 0) + 1
        return formatted_string

    def check(letter):
        if dict_word_booleans.get(letter, None) is None:
            return False
        for condition in dict_word_booleans[letter]:
            if not(condition):
                return True
        return False

    def search():
        for item in dict_word_booleans.values():
            if False in item:
                return False
        return True

    def update_conditions(letter):
        old_condition = dict_word_booleans[letter]
        new_condition = []
        condition_changed = False
        for condition in old_condition:
            if not(condition_changed) and not(condition):
                new_condition.append(True)
                condition_changed = True
            else:
                new_condition.append(condition)
        dict_word_booleans[letter] = new_condition

    dict_word_booleans = {}
    for chars in word.lower():
        old_data = dict_word_booleans.get(chars,[])
        old_data.append(False)
        dict_word_booleans[chars] = old_data
    print("GAME STARTING")
    first_guess = True
    counting_trials = trials
    while counting_trials > 0:
        if first_guess:
            first_guess = False
            inputed_letter = input("Alright, let's do this; Guess a letter {}: ".format(format_output_string())).lower()
        else:
            inputed_letter = input("Almost there; guess another letter {}: ".format(format_output_string())).lower()
        if check(inputed_letter):
            update_conditions(inputed_letter)
            if search():
                print("Correct!, game over, You Won!!\nWORD: {0}\nYou used {1} out of your {2} trials".format(
                    format_output_string(), trials - counting_trials + 1, trials))
                break
            else:
                print("Correct!, {0}, let's continue.".format(format_output_string()))
        else:
            if counting_trials == 1:
                counting_trials -= 1
                print("GAME OVER: You lose:\nWord:{}".format(word))
            else:
                counting_trials -= 1
                print("Oops, You got it wrong, let's do this again, {0} out {1} trials left.".format(counting_trials,
                                                                                                     trials))

print("________________HANGMAN____________________________")
print("CUSTOMIZATION")
hangman(input("Enter the word to be guessed: "), input("Enter the no of trials allowed: "))