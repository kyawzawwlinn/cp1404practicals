from unreliable_car import UnreliableCar


def main():
    # Create an UnreliableCar object
    unreliable_car = UnreliableCar("Old Clunker", 100, 50)

    # Try to drive the car a certain distance
    distance_driven = unreliable_car.drive(30)
    print(f"Attempted to drive 30km, drove {distance_driven}km")

    # Print the car's details
    print(unreliable_car)


if __name__ == '__main__':
    main()
