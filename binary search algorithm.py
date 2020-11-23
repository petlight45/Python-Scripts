def bin_search(list_numbers,number):
    """
        This function checks if a given number is a given list by making use of the binary search algorithm.

        Parameters:
        list_number (list): the list to be checked.

        Return
        bool: True or False depending on whether the given number is in the given list
    """
    def verify_list():
        for obj in list_numbers:
            if type(obj) == int or type(obj) == float:
                pass
            else:
                return False
        return True
    try:
        if len(list_numbers) > 0:
            if not(verify_list()):
                return "invalid input, input must be a list of numbers"
        else:
            return "invalid input, input must not be empty"
    except:
        return "Invalid input"

    list_numbers.sort()
    if len(list_numbers) % 2 == 0:
        centre_left = int(len(list_numbers) /2)-1
        centre_right = int(len(list_numbers) /2)
        if list_numbers[centre_left] == number or list_numbers[centre_right] == number:
            return True
        else:
            if number < list_numbers[centre_left]:
                return bin_search(list_numbers[0:centre_right], number)
            else:
                return bin_search(list_numbers[centre_right:],number)
    else:
        centre = int((len(list_numbers)+1) /2) -1
        if list_numbers[centre] == number:
            return True
        else:
            if len(list_numbers) == 1:
                return False
            else:
                if number < list_numbers[centre]:
                    return bin_search(list_numbers[0:centre], number)
                else:
                    return bin_search(list_numbers[centre+1:],number)

print(bin_search([],4.3))