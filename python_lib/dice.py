from random import randint


class Dice:
    """This class represents the rolling of dice"""

    def __init__(self, sides=6):
        """Initialize the attributes"""
        self.sides = sides

    def roll_dice(self, times):
        """Roll a dice"""
        count = 1
        while count <= times:
            print(f"Rolling for {count} times: {randint(1, self.sides)}")
            count += 1
