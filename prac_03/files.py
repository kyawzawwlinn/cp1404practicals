# Task 1: Write user's name to "name.txt"
user_name = input("Enter your name: ")
with open("name.txt", 'w') as name_file:
    name_file.write(user_name)

# Task 2: Read and print the name from "name.txt"
with open("name.txt", 'r') as name_file:
    stored_name = name_file.read()
    print(f"Your name is {stored_name}")

# Task 3: Read the first two numbers from "numbers.txt" and print their sum
try:
    with open("numbers.txt", 'r') as numbers_file:
        first_number = int(numbers_file.readline().strip())
        second_number = int(numbers_file.readline().strip())
        total = first_number + second_number
        print(f"The sum of the first two numbers is: {total}")
except ValueError:
    print("Invalid data in numbers.txt. Please ensure both lines contain valid numbers.")

# Task 4: Read all numbers from "numbers.txt" and print their total
total_all_numbers = 0
try:
    with open("numbers.txt", 'r') as numbers_file:
        for line in numbers_file:
            total_all_numbers += int(line.strip())
except ValueError:
    print("Invalid data in numbers.txt. Please ensure all lines contain valid numbers.")

print(f"The total of all numbers is: {total_all_numbers}")
