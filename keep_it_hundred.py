def parse(list_working, c_index):
    """
    :param (list)list_working: this is a list that works based on recursion, its value depends on the current recursive depth of the function
    :param (int)c_index: this also depends on the recursive depth
    :return: None
    """
    for vals in list_packed[c_index]:
        for item in [-1,1]:
            temp_list = list_working.copy()
            if len(temp_list) > 0:
                if not True in list([i in (vals,temp_list[-1])[1 if len(vals) > len(temp_list[-1]) else 0] for i in (vals,temp_list[-1])[0 if len(vals) > len(temp_list[-1]) else 1]]):
                    temp_list.append(str(int(vals) * item))
            else:
                temp_list.append(str(int(vals) * item))
            if c_index == len(list_packed) -1:
                if sum([int(i) for i in temp_list]) == 100:
                    if len(working_list) > 0:
                        if temp_list != working_list[-1]:
                            working_list.append(temp_list)
                    else:
                        working_list.append(temp_list)
            else:
                parse(temp_list, c_index+1)9

list_packed = []
for num in range(1,10):
    list_packed.append([])
    list_packed[-1].append(str(num))
    if num != 9:
        list_packed[-1].append("{}{}".format(num, num+1))
working_list = list()
parse(list(), 0)
print(working_list)