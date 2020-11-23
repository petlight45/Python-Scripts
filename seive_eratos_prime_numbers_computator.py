def seive_eratos(lim_num):
    """
      This function computes the list of prime numbers less than a given number by making use of the sieve_eratos technique.

      Parameters:
      lim_num(list): the number whose prime numbers less than it is to be computed

      Return
      list: the list of prime_numbers less than the given numbers
      """
    if lim_num <= 2 and lim_num >= 0:
        return "No prime number less than {0}".format(lim_num)
    elif lim_num > 2:
        pass
    else:
        raise Exception("Invalid input; must be a positive integer!")
    original_list = list(range(2, lim_num))
    for num in original_list:
        if num == 0:
            continue
        for num_2 in range(num+1,lim_num):
            if not num_2 in original_list:
                continue
            if num_2%num == 0:
                original_list[original_list.index(num_2)] = 0
    filtered_list = [i for i in original_list if i != 0]
    text_format = "The list of prime numbers less than {} is {}."
    return text_format.format(lim_num, filtered_list)

print(seive_eratos(10))