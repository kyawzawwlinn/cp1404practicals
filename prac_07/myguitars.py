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


if __name__ == "__main__":
    main()
