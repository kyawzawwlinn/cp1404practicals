from silver_service_taxi import SilverServiceTaxi


def main():
    # Create a SilverServiceTaxi object with a fanciness of 2
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the taxi 18 km
    fancy_taxi.drive(18)

    # Print the taxi's details and the total fare
    print(fancy_taxi)
    print(f"Total fare: ${fancy_taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
