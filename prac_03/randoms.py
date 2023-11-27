# Generating a random number between 1 and 100 (inclusive)
import random

random_number = random.randint(1, 100)
print(random_number)

# 1. What did you see on line 1?
"""I saw a randomly generated integer between 5 and 20 (including both 5 and 20)."""

# 2. What was the smallest number you could have seen, what was the largest?
"""The smallest number could have been 5, and the largest could have been 20."""

# 3. What did you see on line 2?
"""I saw a randomly generated integer from the range [3, 10) with a step of 2."""

# 4. What was the smallest number you could have seen, what was the largest?
"""The smallest number could have been 3, and the largest could have been 9."""

# 5. Could line 2 have produced a 4?
"""No, because the step is 2, and 4 is not in the range [3, 10) with a step of 2."""

# 6. What did you see on line 3?
"""I saw a randomly generated floating-point number between 2.5 and 5.5."""

# 7. What was the smallest number you could have seen, what was the largest?
"""The smallest number could have been 2.5, and the largest could have been 5.5."""
