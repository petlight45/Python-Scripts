def reverse(file_name):
    """
   This function reverse the lines of a file and the characters on each line.

   Parameters:
   file_name(str): the name of the file, must be in the same directory as the main python file

   Return
   None
   """
    try:
        with open(file_name, "r") as file:
            list_inverted = file.readlines()[::-1]
            list_inverted_per_lines = list([i.replace("\n", "")[::-1] + "\n" for i in list_inverted])
            list_inverted_per_lines[-1] = list_inverted_per_lines[-1].replace("\n", "")
            new_file_name = "disodered.txt"
            with open(new_file_name, "w") as file_2:
                for text in list_inverted_per_lines:
                    file_2.write(text)
                print("Operation performed successfully!, file saved as '{}' in the main dir".format(new_file_name))
    except FileNotFoundError:
        print("the specified file does not exist!")

reverse("test_lyrics.txt")