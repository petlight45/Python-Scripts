def compute_divisors(arg):
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


def amicable(arg1, arg2):
    """
    This function checks if a given integer is abundant or not.

    Parameters:
    arg1, arg2 (int): The two integer to be compared

    Return
    str: a remark indicating whether the given integer is amicable or not.
    """
    if type(arg1) != int and type(arg2) != int:
        raise Exception("both inputs must be an integer")
    if arg1 >= 1 and arg2 >= 1:
        pass
    else:
        raise Exception("both inputs must be greater than 1 or equal to 1")
    proper_divisors_1, sum_divisors_1 = compute_divisors(arg1)
    proper_divisors_2, sum_divisors_2 = compute_divisors(arg2)
    if sum_divisors_1 == arg2 and sum_divisors_2 == arg1:
        amicability = True
        return "{0}, The sum of the proper divisors of {1} which are {2} is {3}, The sum of the proper divisors of {4} which are {5} is {6}, since the sum of the proper divisors of the first number is the same as the second number and vice-versa, therefore {7} and {8} are amicable.".format(amicability, arg1,proper_divisors_1,sum_divisors_1,arg2,proper_divisors_2,sum_divisors_2,arg1,arg2)
    else:
        amicability = False
        return "{0}, The sum of the proper divisors of {1} which are {2} is {3}, The sum of the proper divisors of {4} which are {5} is {6}, since the sum of the proper divisors of the first number is not the same as the second number in both cases vice-versa, therefore {7} and {8} are not amicable.".format(amicability, arg1,proper_divisors_1,sum_divisors_1,arg2,proper_divisors_2,sum_divisors_2,arg1,arg2)


print(amicable(220,284))