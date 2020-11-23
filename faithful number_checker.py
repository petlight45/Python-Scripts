from itertools import combinations
def faithful(n):
    """
        This function computes and return the nth faithful number where n is given

        Parameters:
        n (int): represents the nth faithful number to compute

        Return
        int: The nth faithful number computed
    """

    if type(n) == int:
        if n < 1:
            return "Invalid Input!, input must be greater than 0"
    else:
        return "Invalid input!, input must be integer"

    def filter_combinations(list_to_sort):
        """
            This function takes a list of tuples containing integers, it the sorts the list in ascending order by making use of the integers in each tuples.

            Parameters:
            list_to_sort (list): a list of tuples containing integers, e.g [(0,2),(1,2), (0,2,4,5)]

            Return
            list: the sorted list
        """
        def check_lower(args1, args2):
            """
            This function checks which is lower between two given tuple of integers, the sorting value of each tuple is calculated by taking the sum of 7 raise to the power of each integers in the tuple,\
            e.g supposing the function takes input of [0,2] and (1,2)  now 7^0 + 7^2 =  50, 7^1 + 7^2 = 56, therefore [1,2] > [0,2], the function will then a boolean value depending on which is lower.
            Note: sometimes args1 or args2 might be an integer rather than a tuple of integer, but same condition for sorting still follows
            Parameters:
            args1 (list): an integer or a list of integers
            args2 (list): an integer or a list of integers

            Return:
            boolean: if args2 is lower, returns True else returns 1
            """
            list_sum = []
            for values in [args1, args2]:
                sum = 0
                try:
                    for integer in values:
                        sum += pow(7, integer)
                # an error containing block in case the variable "values" is an integer
                except TypeError:
                    sum += pow(7, values)
                list_sum.append(sum)
            if list_sum[1] < list_sum[0]:
                return True
            else:
                return False

        filtered_list = list()
        length_list_to_sort = len(list_to_sort)
        #the sorting lines of code
        for num in range(length_list_to_sort):
            lowest = None
            for index, combo in enumerate(list_to_sort):
                if lowest is None:
                    lowest = index
                else:
                    if check_lower(list_to_sort[lowest], combo):
                        lowest = index
            filtered_list.append(list_to_sort[lowest])
            list_to_sort.remove(list_to_sort[lowest])
        return filtered_list

    def compute_list_faithful_powers():
        """
                This function computes the list of powers of the faithful number sequence e.g for a faithful sequence (1,7,8,49), it list of power is [[0], [1], [0,1],[2]], the function doesn't take any parameter since it has access to the parameter 'n' taken in by its parent function

                Parameters:
                None

                Return
                list: The list of powers of the faithful sequence
            """
        list_faithful_powers = []
        nth_faitful_rached = False
        current_num = 0
        while True:
            computed_list = list(range(current_num+1))
            if len(computed_list) == 1:
                list_faithful_powers.append(computed_list)
                if n == 1:
                    break
            else:
                for num in range(1, len(computed_list)+1):
                    list_filtered = filter_combinations(list(combinations(computed_list, num)))
                    for item in list_filtered:
                        if not(list(item) in list_faithful_powers):
                            list_faithful_powers.append(list(item))
                            if n == len(list_faithful_powers):
                                nth_faitful_rached = True
                                break
                    if nth_faitful_rached:
                        break
                if nth_faitful_rached:
                    break
            current_num += 1
        return list_faithful_powers

    #this below line of codes initiates the major function calling operation
    sum_power = 0
    for power in compute_list_faithful_powers()[n-1]:
        sum_power += pow(7,power)
    return sum_power

print(faithful(0))