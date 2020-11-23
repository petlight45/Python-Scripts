def abundant(arg):
    """
    This function checks if a given integer is abundant or not.

    Parameters:
    args (int): The integer to be checked.

    Return
    str: a remark indicating whether the given integer is abundant or not.
    """
    if type(arg) != int:
        raise Exception("input must be an integer")
    if arg < 1:
        raise Exception("Input must be greater than 1")
    proper_divisors, sum_divisors = sum_abundant(arg)
    text_format = "{0}, {1} is {2}an abundant number because the sum of it's proper divisors {3} which is {4} is {5} than {6} itself."
    if sum_divisors > arg:
        abundancy = True
        return text_format.format(abundancy, arg, "", proper_divisors, sum_divisors, "greater", arg)
    else:
        abundancy = False
        return text_format.format(abundancy, arg, "not ", proper_divisors, sum_divisors, "lower", arg)


def sum_abundant(arg):
    """
        This function computes the proper divisors and the sum of the proper divisors of a given integer.

        Parameters:
        args (int): The integer to work with.

        Return
        list: list of proper divisors.
        int: sum of proper divisors.
        """
    sum_divisors = 0
    divisors = []
    for num in range(1, arg):
        if arg % num == 0:
            divisors.append(num)
            sum_divisors += num
    return divisors, sum_divisors


print(abundant(200))