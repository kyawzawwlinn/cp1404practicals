def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"Result: {result:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {result:.2f} C")
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
