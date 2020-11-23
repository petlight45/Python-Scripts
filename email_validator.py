def validate_email(email_addr):
    """
        This function validates a given email address.

        Parameters:
        email_addr (str): The email address to validate.

        Return
        str: a remark indicating whether the email is valid or not.
        """
    if type(email_addr) == str:
        if email_addr.count("@") == 1 and email_addr.count(".") > 0:
            pass
        else:
            return "Invalid email address; A typical email address should have char '@' occurring once and char '.' occurring at least once"
    else:
        return "Invalid input: must be a string."
    #Validating the first segment
    segment_1 = email_addr[0:email_addr.index("@")]
    special_char = ".-_"
    if segment_1.islower() and segment_1.replace(".", "").replace("-", "").replace("_","").isalnum():
        if segment_1.count(".") > 1:
            return "Invalid email address; the address prefix '{}' can only contain a single dot".format(segment_1)
        for id, char in enumerate(segment_1):
            if char in special_char:
                try:
                    if segment_1[id+1].isalnum():
                        pass
                    else:
                        return "Invalid email_address; special characters in the address prefix '{}' should be followed by either a number or alphabet".format(segment_1)
                except IndexError:
                    return "Invalid email_address; special characters in the address prefix '{}' should be followed by either a number or alphabet".format(
                        segment_1)

    else:
        return "Invalid email_address; the address prefix '{}' should be in lower-case and should be alphanumeric with the exeption of the allowed special charcters '{}'".format(segment_1,special_char)
    #Validating the second segment
    segment_2 = email_addr[len(segment_1)+1: email_addr.find(".",len(segment_1)+1)]
    special_char = "-"
    if segment_2.lower() and segment_2.replace("-","").isalnum():
        for id, char in enumerate(segment_2):
            if char in special_char:
                try:
                    if segment_2[id + 1].isalnum():
                        pass
                    else:
                        return "Invalid email_address; special characters in the address' second segment '{}' should be followed by either a number or alphabet".format(
                            segment_2)
                except IndexError:
                    return "Invalid email_address; special characters in the address' second segment '{}' should be followed by either a number or alphabet".format(
                        segment_2)
    else:
        return "Invalid email_address; the address' second segment '{}' should be in lower-case and should be alphanumeric with the exeption of the allowed special charcter '-'".format(
            segment_2)
    #Validating the third segment
    segment_3 = email_addr[len(segment_1)+1 + len(segment_2)+1:]
    if segment_3.replace(".", "").isalpha():
        available_dots = segment_3.count(".")
        dots_counted = 0
        for id, char in enumerate(segment_3):
            if char == ".":
                dots_counted += 1
                if dots_counted == available_dots:
                    try:
                        if len(segment_3[id+1:]) == 2 or len(segment_3[id+1:]) == 3:
                            pass
                        else:
                            return "Invalid email_address; the number of characters after the last dot in the address third segment '{}' should be either 2 or 3".format(segment_3)
                    except IndexError:
                        return "Invalid email_address; the number of characters after the last dot in the address third segment '{}' should be either 2 or 3".format(
                            segment_3)
                else:
                    if segment_3[id+1] == ".":
                        return "Invalid email address; consective dots is not allowed in the address third segment '{}'".format(segment_3)
    else:
        return "Invalid email_address; the address third segment '{}' should be of only alphabetical characters with the exeption of '.'".format(
            segment_3)
    return "The email address is valid"

print(validate_email("petlight45@yahoo.com"))
