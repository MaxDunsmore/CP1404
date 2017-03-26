"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    if MIN_LENGTH > len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for character in password:
        lower_check = character.islower()
        if lower_check is True:
            count_lower += 1
        upper_check = character.isupper()
        if upper_check is True:
            count_upper += 1
        digit_check = character.isdigit()
        if digit_check is True:
            count_digit += 1
        if character in SPECIAL_CHARACTERS:
            count_special += 1
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED is True:
        if count_special == 0:
            return False
    return True


main()
