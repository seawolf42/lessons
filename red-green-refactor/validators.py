def password(value):
    if not isinstance(value, str):
        return False
    if len(value) < 8:
        return False
    if value.upper() == value:
        return False
    if value.lower() == value:
        return False
    has_digits = False
    for c in value:
        if c.isdigit():
            has_digits = True
            continue
    if not has_digits:
        return False
    return True
