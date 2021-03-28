import re


# Букавы, нижние подчеркивания, цифры, точки (но чтобы не заканчивалось на точку и нижнее подчеркивание)
def check_left_part(l_part):
    found_str = re.fullmatch(r"^[a-zA-Z](?:[a-zA-Z\d_.][a-zA-Z\d])*(?:[a-zA-Z\d])*$", l_part)
    if found_str is not None and found_str.string == l_part:
        return True
    return False


# тут просто списки по 5 элементов
def check_right_part(r_part):
    split_parts = str.split(r_part, ".")
    try:
        tld = split_parts.pop()
    except IndexError:
        return False
    matched_tld = re.fullmatch(r"^(?:com|ru|org|net|su)$", tld)
    if matched_tld is not None and matched_tld.string == tld and len(split_parts) != 0:
        sld = split_parts.pop()
        while len(split_parts) != 0:
            sld = split_parts.pop() + sld
        matched_sld = re.fullmatch(r"^(?:stud.kpfu|mail|gmail|inbox|wikipedia)$", sld)
        if matched_sld is not None and matched_sld.string == sld:
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
