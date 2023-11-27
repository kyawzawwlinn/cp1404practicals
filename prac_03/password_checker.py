MINIMUM_LENGTH = 2
MAXIMUM_LENGTH = 6
SPECIAL_CHARACTERS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MINIMUM_LENGTH} and {MAXIMUM_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARACTERS_REQUIRED:
        print(f"\tand 1 or more special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check length
    if not MINIMUM_LENGTH <= len(password) <= MAXIMUM_LENGTH:
        return False

    # Count variables
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # Count each kind of character
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif SPECIAL_CHARACTERS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1

    # Check if any of the 'normal' counts are zero
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # If special characters are required, check the count of those
    if SPECIAL_CHARACTERS_REQUIRED and count_special == 0:
        return False

    # If we get here, the password is valid
    return True


# Run the main function
main()
