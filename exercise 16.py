import math
number = float(input("Enter a number: "))
answer = math.log10(number)/math.log10(int(input("Enter the power to check for: ")))
if type(answer) == float:
    if str(answer)[str(answer).find(".")+1:] == "0":
        print("{} is a power of 2".format(number))
    else:
        print("{} is not a power of 2".format(number))
else:
    print("{} is not a power of 2".format(number))