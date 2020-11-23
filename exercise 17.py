def check_additive(list):
    count = 0
    validation = False
    for integer in list:
        if count > 1:
            if (list[count-2] + list[count-1]) == list[count]:
                pass
            else:
                break
        count += 1
    else:
        validation = True
    return validation

list_integers = []
print(check_additive(list_integers))