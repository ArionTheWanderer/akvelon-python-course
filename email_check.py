import re


def check_left_part(l_part):
    found = re.search(r"^[a-bA-B0-9_.]+$", l_part)
    if found == l_part:
        return True
    return False

def check_right_part(r_part):
    splitted_parts = re.split()