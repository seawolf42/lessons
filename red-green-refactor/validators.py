import re


valid_regex = re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')


def password(value):
    if not isinstance(value, str):
        return False
    if valid_regex.match(value):
        return True
    return False
