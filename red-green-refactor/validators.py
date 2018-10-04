def password(value):
    if not isinstance(value, str):
        return False
    if len(value) < 8:
        return False
    if value.upper() == value:
        return False
    if value.lower() == value:
        return False
    if len(set(value).intersection(set('1234567890'))) == 0:
        return False
    return True
