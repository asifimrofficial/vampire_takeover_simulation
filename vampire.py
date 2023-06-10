import random

class Vampire:
    def __init__(self, health, age, position):
        self.health = health
        self.age = age
        self.position = position

    def move(self, map_size):
        # Randomly move the vampire up to 8 spaces in any direction
        x, y = self.position
        new_x = random.randint(max(0, x - 8), min(map_size, x + 8))
        new_y = random.randint(max(0, y - 8), min(map_size, y + 8))
        self.position = (new_x, new_y)

    def bite(self):
        # The vampire bites another vampire, losing 20 health
        self.health -= 20
   
    def __str__(self):
        return f"Vampire: Health={self.health}, Age={self.age}, Position={self.position}"
