class Guitar:
    """Represent a guitar with specific attributes."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance.

        name: str, the name of the guitar
        year: int, the year the guitar was made
        cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return how old the guitar is in years."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        """Compare guitars based on the year for sorting."""
        return self.year < other.year
