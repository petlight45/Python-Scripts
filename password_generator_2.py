import random

def password_generator(arg_1):
    """
    This function generates and return a password of given length

    Parameters:
    arg1 (int): Length of password to be generated

    Return
    str: The password generated
    """
    chars = "abcdefghijklmnopqrstuvwxyz01234567890"
    case_upper = [True, False]
    while True:
        generated_password = ""
        for num in range(arg_1):
            random.shuffle(case_upper)
            if case_upper[0]:
                generated_password += random.choice(chars).upper()
            else:
                generated_password += random.choice(chars)
        if generated_password.isalnum() and not(generated_password.islower()) and not(generated_password.isupper()):
            break
    if arg_1 < 8:
        return "{}, your password is weak!".format(generated_password)
    else:
        return generated_password


print(password_generator(4))