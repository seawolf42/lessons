def password(value):
    if not isinstance(value, str):
        return False
    if len(value) < 8:
        return False
    if value.upper() == value:
        return False
    return True
