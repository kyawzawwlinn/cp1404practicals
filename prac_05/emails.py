"""
User Emails and Names
Estimate: 40 minutes
Actual:   47 minutes
"""


def extract_name(email):
    username = email.split('@')[0]
    name_parts = [part.title() for part in username.split('.')]
    return ' '.join(name_parts)


def main():
    user_data = {}

    while True:
        email = input("Email: ").strip()
        if not email:
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation == '' or confirmation == 'y':
            user_data[email] = name
        else:
            custom_name = input("Name: ").strip()
            user_data[email] = custom_name

    print("\nUser Data:")
    for email, name in user_data.items():
        print(f"{name} ({email})")


main()
