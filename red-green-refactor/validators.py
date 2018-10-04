def password(value):
    if not isinstance(value, str):
        return False
    if len(value) < 8:
        return False
    return True
