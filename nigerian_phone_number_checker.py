import re

def is_Nigerian(args1):
    """
        This function checks if a given number is a Nigerian phone number.

        Parameters:
        args1 (str): the phone number to be checked.

        Return
        str: a remark that indicates if the phone number is Nigerian or not.
    """
    if len(args1) == 0:
        return "Invalid input!, input must not be empty."
    if (args1.isalnum() and not(args1.isnumeric())) or args1.isalpha():
        return "Invalid Input!, input must be a string of numbers."
    #creating a matching pattern for nigerian numbers by making use of regular expressions
    pattern_match = re.compile(r"(\+234|0)(0?)(8[01]|[79]0)(\d{8}$)")
    matches = pattern_match.match(args1)
    if matches != None:
        if matches.group(2) == "0":
            return "True, {0} is a Nigerian number but you don't have to add the '0' that follows the country code, conventionally the number should be {1}".format(args1, "{0}{1}{2}".format(matches.group(1),matches.group(3),matches.group(4)))
        else:
            return "True, {0} is a Nigerian number".format(args1)
    else:
        return "False, {0} is not a Nigerian number".format(args1)

print(is_Nigerian("+23409060990102"))