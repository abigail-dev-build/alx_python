# Write a Python function called validate_password that takes a password as input and performs the following checks:
# The password should be at least 8 characters long.
# The password should contain at least one uppercase letter, one lowercase letter, and one digit.
# The password should not contain spaces.
# Returns True if the password passes all the checks, and False otherwise.

def validate_password(password):
    # Check password length
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


print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))

