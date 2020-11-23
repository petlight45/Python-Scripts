def wrapper(paragraph, max_char_per_line):
    """
       This function wraps a paragraph into a given maximum no of characters per line.

       Parameters:
       paragraph (str): The paragraph to work with.
       max_char_per_line (int): The maximum no of charcter per line.

       Return
       str: the wrapped text.
    """
    #Validation
    if type(paragraph) == str and type(max_char_per_line) == int:
        pass
    else:
        raise Exception("Invalid Input: paragraph must be a string, max_char_per_line must be an integer")
    offset = 0
    list_filtered = []
    temp_text = ""
    for text in paragraph:
        if offset == max_char_per_line or text=="\n":
            offset = 0
            list_filtered.append(temp_text.replace("\n", "") + "\n")
            temp_text = ""
        if text != "\n":
            temp_text += text
            offset += 1
    else:
        if temp_text != "":
            list_filtered.append(temp_text)
    return "".join(list_filtered)

working_text = "The family of two\nwent out to play."
print(wrapper(working_text, 10))

