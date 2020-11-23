import random
def gen_password(strength):
    password = []
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "&$#@!%^&*()-+=[]?/.,><~`"
    if strength == "strong":
        length_ucase = random.randrange(2,5)
        length_lcase = random.randrange(3,7)
        length_numbers = random.randrange(2,4)
        length_symbols = random.randrange(1,6)
    elif strength == "medium":
        length_ucase = random.randrange(2,4)
        length_lcase = random.randrange(2,5)
        length_numbers = random.randrange(2,4)
        length_symbols = 0
    else:
        length_ucase = random.randrange(2,4)
        length_lcase = random.randrange(2,5)
        length_numbers = 0
        length_symbols = 0
    for num in range(0,length_ucase):
        password += (alphabets[random.randrange(0,len(alphabets))]).upper()
    for num in range(0,length_lcase):
        password += alphabets[random.randrange(0,len(alphabets))]
    for num in range(0,length_numbers):
        password += numbers[random.randrange(0,len(numbers))]
    for num in range(0,length_symbols):
        password += symbols[random.randrange(0,len(symbols))]
    random.shuffle(password)
    password_1 = ""
    for char in password:
        password_1 += char
    return password_1




if __name__ == "__main__":
    print("---------------Password Generator--------------------")
    difficulty = (input("Enter your password strength: \na.Strong \nb.Medium\nc.Weak\nInput Your Reply: ")).lower()
    if difficulty == "a":
        p_strength = "strong"
    elif difficulty == "b":
        p_strength = "medium"
    elif difficulty == "c":
        p_strength = "weak"
    else:
        print("Invalid Reply")
        exit()
    password = gen_password(p_strength)
    print("The generated password is {}".format(password))

