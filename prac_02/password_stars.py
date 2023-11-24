def main():
    minimum_length = 6
    password = get_password()

    if len(password) > minimum_length:
        print("*" * len(password))


def get_password():
    password = input("Enter a password:")
    return password


main()