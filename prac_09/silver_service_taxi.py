from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancier version of a Taxi with additional charges."""
    flagfall = 4.50  # class variable for extra charge per new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Modify price per km based on fanciness

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
