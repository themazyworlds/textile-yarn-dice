"""Sample Dice Rolling Yarn for testing Textile package manager."""

import random
from needle import Yarn, strand


class Dice(Yarn):
    """Dice capability yarn for generating random rolls."""

    @strand
    def roll_dice(self, sides: int = 6) -> int:
        """Roll a dice with the given number of sides."""
        return random.randint(1, max(1, sides))
