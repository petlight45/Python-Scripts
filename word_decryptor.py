def decryptor(text, key):
    """
        This function decrypts a coded word by making use of an offset number that corresponds how much the actual character is away from its encrypted value in the\
        english alphabet, it be may leftward or rightward direction depending on the sign of the offset number, positive for right, negative for left.

        Parameters:
        text (str): The text that is to be decrypted
        key (int): an offset number that corresponds how much the actual character is away from its encrypted value in the english alphabet

        Return
        str : the decrypted text
        """
    # Validation codes
    if not type(text) == str:
        return "Invalid input(s); text must be a string"
    try:
        key = int(key)
    except:
        return "Invalid input(s); key must be an integer"

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    decrypted_text = ""
    for char in text:
        if not(char.isalpha()):
            decrypted_text += char
            continue
        if char.isupper():
            isupper = True
        else:
            isupper = False
        char = char.lower()
        print(len(alphabets), alphabets.find(char))
        if key > 0 and (len(alphabets)-1-alphabets.find(char) < key):
            selecting_key = key - ((len(alphabets)-1) - (alphabets.find(char)) + 1)
        else:
            selecting_key = alphabets.find(char) + key
        if isupper:
            decrypted_text += alphabets[selecting_key].upper()
        else:
            decrypted_text += alphabets[selecting_key].lower()
    return "The decrypted text of '{0}' by using the key '{1}' is '{2}'.".format(text, key, decrypted_text)

print(decryptor("Rovvy pbyw dro ydrob csno....", "u"))