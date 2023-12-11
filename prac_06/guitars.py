from guitar import Guitar


def main():
    """Program that uses the Guitar class."""
    print("My guitars!")
    guitars = []

    while True:
        name = input("Name: ")
        if not name:
            break

        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage(2022) else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")
    else:
        print("You haven't added any guitars.")


# Call the main function explicitly
main()
