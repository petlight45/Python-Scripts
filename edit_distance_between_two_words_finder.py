def find_edit_dist(arg1, arg2):
    """
        This function computes the edit distance between two given strings.

        Parameters:
        arg1 (str): The first string .
        arg2 (str): The second string.

        Return
        int: the edit distance.
        """
    def parse_words(str_1, str_2, offset):
        """
        This function filters two given strings to the same length by making use of some guidelines.

        Parameters:
        str_1 (str): The longest string .
        str_2 (str): The lowest string.
        offset(int): this indicates the number of dummy(filtering) characters that will be prefixed to either the lowest_string or longest string

        Return
        str, str: the two filtered strings.
        """
        chars = "01" #dummy characters
        prefix = ""
        for num in range(abs(offset)):
            for char in chars:
                if str_1[num] != char:
                    prefix += char
                    break
        if offset < 0:
            str_1 = prefix + str_1
        else:
            str_2 = prefix + str_2
        suffix_length = abs(len(str_2)-len(str_1))
        if len(str_1) == len(str_2):
            return (str_1, str_2)
        lowest_str = str_1
        highest_str = str_2
        if len(str_1) > len(str_2):
            lowest_str = str_2
            highest_str = str_1
        suffix = ""
        for num in range(suffix_length):
            for char in chars:
                if highest_str[len(lowest_str)+num] != char:
                    suffix += char
                    break
        lowest_str+= suffix
        return (lowest_str, highest_str)

    #assigning the strings according to their length
    greatest = arg1
    smallest = arg2
    if len(arg2) > len(arg1):
        greatest = arg2
        smallest = arg1

    #looping round the greatest string in order to check if there is any cluster of string that matches any cluster in the lowest string, this is done in order to perform an offset on the lowest string
    position_offset = 0
    #starting the loop from the highest possible cluster we can have
    for num in range(len(smallest), 0, -1):
        for id in range(len(greatest)):
            if len(greatest[id:]) >= num:
                try:
                    char = greatest[id:id + num]
                except IndexError:
                    char = greatest[id:]
                if char in smallest:
                    position_offset = greatest.index(char) - smallest.index(char)
                    break
            else:
                break
        if position_offset != 0:
            break
    #calling a function that will filter the strings and makes both strings of the same length
    s_a, s_b = (parse_words(greatest,smallest,position_offset))
    edit_distance = 0
    #creating a loop that will check discrepancy between the two returned strings
    for id in range(len(s_a)):
        if s_a[id] != s_b[id]:
            edit_distance += 1
    return edit_distance

print(find_edit_dist("goat", "float"))