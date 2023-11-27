import random

MAXIMUM_INCREASE = 0.175  # 17.5%
MAXIMUM_DECREASE = 0.05  # 5%
MINIMUM_PRICE = 1.0
MAXIMUM_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_simulation_output.txt"

price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

print(f"Starting price: ${price:,.2f}")
print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

while MINIMUM_PRICE <= price <= MAXIMUM_PRICE:
    price_change = 0

    if random.randint(1, 2) == 1:

        price_change = random.uniform(0, MAXIMUM_INCREASE)
    else:
        price_change = random.uniform(-MAXIMUM_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1

    # Print to console
    print(f"On day {number_of_days} price is: ${price:,.2f}")

    # Print to file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file
out_file.close()
