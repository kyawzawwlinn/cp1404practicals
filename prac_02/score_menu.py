def get_valid_score():
    score = None
    while score is None:
        try:
            score = float(input("Enter a valid score (0-100 inclusive): "))
            if not 0 <= score <= 100:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")
    return score

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    print("*" * int(score))

def main():
    print("Welcome to the Score Menu!")
    choice = ""

    while choice != "Q":
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input(">>> ").upper()

        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            try:
                result = determine_score_status(user_score)
                print(f"Result: {result}")
            except NameError:
                print("Please enter a score first using option (G).")
        elif choice == "S":
            try:
                print_stars(user_score)
            except NameError:
                print("Please enter a score first using option (G).")
        elif choice == "Q":
            print("Thank you for using the Score Menu. Goodbye!")
        else:
            print("Invalid option. Please choose a valid option.")

main()