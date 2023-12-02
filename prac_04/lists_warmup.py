numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)

print(numbers[0])  # Output: 3
print(numbers[-1])  # Output: 2
print(numbers[3])  # Output: 1
print(numbers[:-1])  # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # Output: [1]
print(5 in numbers)  # Output: True
print(7 in numbers)  # Output: False
print("3" in numbers)  # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Write Python expressions (in your Python file) to achieve the following:
numbers = ["ten", 1, 4, 1, 5, 9, 1]
# Change the first element of numbers to "ten"
print(numbers[0])  # output: ten
# Change the last element of numbers to 1
print(numbers[-1])  # output : 1
# Get all the elements from numbers except the first two
print(numbers[2:])  # output : [4, 1, 5, 9, 1]
# Check if 9 is an element of numbers
print(9 in numbers)  # output : True
