import random

class Die:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):

        rolled = random.randint(1, self.sides)
        return rolled