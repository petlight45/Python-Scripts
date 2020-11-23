def to_mandarin(number):
    dict_translator = {
        0: "ling",
        1: "yi",
        2: "er",
        3: "san",
        4: "si",
        5: "wu",
        6: "liu",
        7: "qi",
        8: "ba",
        9: "jiu",
        10: "shi"
    }
    if number <= 10:
        return dict_translator[number]
    else:
        quotient = int(number / 10)
        remainder = number % 10
        if quotient == 0 or quotient == 1:
            quotient = -1
        if remainder == 0:
            remainder = -1
        translated = " ".join([i for i in "{} {} {}".format(dict_translator.get(quotient, ""), dict_translator[10], dict_translator.get(remainder, "")).split(" ") if i != ""])
print(to_mandarin(99))