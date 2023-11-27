"""CP1404/CP5632 - Practical Answer the following questions: 1. When will a ValueError occur? - A ValueError will
occur if I enter something that is not a whole number (integer) when prompted for the numerator or denominator.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if I enter 0 as the denominator, which would mean I'm trying to divide by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError? - Yes, I can change the code to check
if the denominator is 0 before performing the division. If it is 0, the program will print an error message,
preventing the ZeroDivisionError."""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is 0 before performing the division
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
