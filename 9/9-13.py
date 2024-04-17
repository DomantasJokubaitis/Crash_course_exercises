from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = self.sides
        while x > 0:
            rolled = randint(1, self.sides)
            print(rolled)
            x -= 1

x = Die()
x.roll_die()
print()
x = Die(10)
x.roll_die()
print()
x = Die(20)
x.roll_die()
print()


