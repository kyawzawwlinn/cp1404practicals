def print_hills(num, symbol1, symbol2):
    for i in range(1, num + 1):
        print(''.join([symbol1 if j % 2 == 0 else symbol2 for j in range(i)]))
    for i in range(num - 1, 0, -1):
        print(''.join([symbol1 if j % 2 == 0 else symbol2 for j in range(i)]))


# Example usage:
print_hills(4, "H", "!")
