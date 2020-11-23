def bin_adder(a,b):
    """
       This function adds two given binary numbers together.

       Parameters:
       a(int, float): first binary number.
       b(int, float): second binary number.

       Return
       str: a remark containing the sum of the binary numbers specified.
       """
    #Verification
    try:
        str_a = str(float(a))
        str_b = str(float(b))
    except:
        raise Exception("invalid input: it must be a number")
    for num in str_a.replace(".", ""):
        if int(num) > 1:
            raise Exception("both inputs must be a binary number")
    for num in str_b.replace(".", ""):
        if int(num) > 1:
            raise Exception("both inputs must be a binary number")

    diff_dec = len(str_a[str_a.index(".")+1:]) - len(str_b[str_b.index(".")+1:])
    if diff_dec > 0:
        str_b += "0" * diff_dec
    else:
        str_a += "0" * (diff_dec * -1)
    diff_whole = len(str_a[:str_a.index(".")]) - len(str_b[:str_b.index(".")])
    if diff_whole > 0:
        str_b = ("0" * diff_whole) + str_b
    else:
        str_a = ("0" * (diff_whole * -1)) + str_a
    quotient = 0
    sum = ""
    index = len(str_a) -1
    while True:
        if index < 0:
            add_a = add_b = 0
        else:
            if str_a[index] == ".":
                sum += "."
                index -= 1
                continue
            add_a = int(str_a[index])
            add_b = int(str_b[index])
        summed = add_a + add_b + quotient
        if index < 0:
            if summed == 1:
                sum += "1"
            break
        else:
            if summed > 1:
                sum += str(summed%2)
                quotient = summed//2
            else:
                sum += str(summed)
                quotient = 0
        index -= 1
    text_format = "The sum of the two binary numbers {0} and {1} is {2}."
    if sum[::-1][-2:] == ".0":
        return text_format.format(a,b,sum[::-1][:-2])
    else:
        return text_format.format(a,b,sum[::-1])

print(bin_adder(1,1))