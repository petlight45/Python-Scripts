def compressor(string_num):
    """
    This function compresses a given string of numbers into a tuple of tuples, with each tuples containing a distinct number in the string and the no of times it occured in the string.

    Parameters:
    string_num (str): The string to compress.

    Return
    tuple: the compressed string.
    """
    try:
        if not (string_num.isnumeric()):
            return "Invalid Input: must be a string of numbers only"
    except:
        return "Invalid Input!: must be a string"
    dict_count = {}
    for num in string_num:
        dict_count[int(num)] = dict_count.get(int(num), 0) + 1
    return tuple(dict_count.items())



print(compressor("12345432566"))
