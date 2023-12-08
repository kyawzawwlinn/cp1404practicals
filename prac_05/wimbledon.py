"""

Wimbledon Champions
Estimate: 60 minutes
Actual:   75 minutes
File: wimbledon.py

"""


def read_wimbledon_data(filename):
    wimbledon_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data_row = line.strip().split(',')
            wimbledon_data.append(data_row)
    return wimbledon_data


def count_champions(wimbledon_data):
    champions_count = {}
    for row in wimbledon_data:
        champion_name = row[0]
        champions_count[champion_name] = champions_count.get(champion_name, 0) + 1
    return champions_count


def list_countries(wimbledon_data):
    countries_set = set(row[2] for row in wimbledon_data)
    return sorted(countries_set)


def display_results(champions_count, countries_set):
    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon:")
    print(', '.join(countries_set))


def main():
    filename = "wimbledon.csv"
    wimbledon_data = read_wimbledon_data(filename)
    champions_count = count_champions(wimbledon_data)
    countries_set = list_countries(wimbledon_data)
    display_results(champions_count, countries_set)


main()
