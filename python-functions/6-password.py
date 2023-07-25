def validate_password(password):
    if len(password) < 8:
        return False

    HAS_UPPERCASE = False
    HAS_LOWERCASE = False
    HAS_DIGIT = False

    for character in password:
        if character.isupper():
            HAS_UPPERCASE = True
        elif character.islower():
            HAS_LOWERCASE = True
        elif character.isdigit():
            HAS_DIGIT = True

    if not (HAS_UPPERCASE and HAS_LOWERCASE and HAS_DIGIT):
        return False

    if " " in password:
        return False

    return True
