from guitar import Guitar


def load_guitars(file_name):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name, year, cost = parts[0], int(parts[1]), float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        pass
    return guitars


def write_guitars(file_name, guitars):
    """Write guitars to a file."""
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")


def get_new_guitar():
    """Get input from the user to create a new guitar."""
    name = input("Enter the name of the guitar: ")
    year = int(input("Enter the year the guitar was made: "))
    cost = float(input("Enter the cost of the guitar: "))
    return Guitar(name, year, cost)


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)


def main():
    file_name = "guitars.csv"
    guitars = load_guitars(file_name)

    # Display original list
    print("Original list of guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    # Display sorted list
    print("\nSorted list of guitars by year:")
    display_guitars(guitars)

    # Ask the user for new guitars
    while True:
        add_another = input("Do you want to add another guitar? (y/n): ").lower()
        if add_another != 'y':
            break
        new_guitar = get_new_guitar()
        guitars.append(new_guitar)

    # Write the updated list to the file
    write_guitars(file_name, guitars)

    # Display the final list
    print("\nFinal list of guitars:")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
