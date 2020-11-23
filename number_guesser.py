def guess_no(trials, no):
    """
    This function gives a user an attempt to guess a given number correctly within the specified trial.

    Parameters:
    trials (int): The no of trials allowed for the number to be guessed correctly.
    no (int): The number that is to be guessed.

    Return
    None: in case the conditions required of the input values are not satisfied.
    str: in case the user guess the number correctly within the given trial; an applauding remark.
    int: in case the user does not guess the number correctly within the given trial; the absolute difference between the final guess and the actual value.
    """
    if type(trials) == int and trials>0 and type(no) == int:
        previous_guess = None
        for num in range(trials):
            if previous_guess is None:
                previous_guess = int(input("Guess a number: "))
                if previous_guess == no:
                    return "{0}, Guessed correctly!".format(previous_guess)
            else:
                hint = "higher"
                if previous_guess > no:
                    hint = "lower"
                previous_guess = int(input("Almost there, guess {}: ".format(hint)))
                if previous_guess == no:
                    return "{0}, Guessed correctly!".format(previous_guess)
        return abs(no - previous_guess)
    else:
        return "Invalid Input!"

if __name__ =="__main__":
    print(guess_no(10, 7))