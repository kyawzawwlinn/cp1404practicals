class ProgrammingLanguage:
    """Represent a programming language with specific attributes."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance.

        name: str, the name of the programming language
        typing: str, the typing nature of the programming language (Static/Dynamic)
        reflection: bool, whether the programming language supports reflection or not
        year: int, the year the programming language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

