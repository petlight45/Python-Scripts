import itertools

def power_set(args):
    """
        This function returns a power list of a given list.

        Parameters:
        args (list): The list that its power list is to be found.

        Return
        list: the power list of the given list.
        """
    #Validation codes
    if type(args) == list:
        if len(args) == 0:
            return "Invalid input, the list must not be empty"
    else:
        return "Invalid input; the function accepts only a list as input"
    list_powerset = [[]]
    for numbers in range(1,len(args)+1):
        for data in list(itertools.combinations(args, numbers)):
            if not list(data) in list_powerset:
                list_powerset.append(list(data))
    return "The power list of {} is {}.".format(args, list_powerset)

print(power_set([]))