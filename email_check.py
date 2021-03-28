import re


def check_left_part(l_part):
    found = re.search(r"^[a-bA-B][a-bA-B0-9_.]*$", l_part)
    if found == l_part:
        return True
    return False


def check_right_part(r_part):
    split_parts = str.split(r_part, ".")
    try:
        tld = split_parts.pop()
    except IndexError:
        return False
    if re.search(r"^(?:com|ru|org|net|su)$", tld) == tld and len(split_parts) != 0:
        sld = split_parts.pop()
        while len(split_parts) != 0:
            sld += split_parts.pop()
        if re.search(r"^(?:stud.kpfu|mail|gmail|inbox|wikipedia)$", tld) == tld:
            return True
    return False


def check_email(email):
    email_parts = str.split(email, "@")
    if len(email_parts) != 2:
        return False
    if check_right_part(email_parts.pop()) and check_left_part(email_parts.pop()):
        return True
    return False


if __name__ == '__main__':
    email = "kukaracha000@gmail.com"
    is_right = check_email(email)
    if is_right:
        print("Valid email")
    else:
        print("Invalid email")
