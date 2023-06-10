import random

class Human:
    def __init__(self, health, age, position):
        self.health = health
        self.age = age
        self.position = position

    def move(self, map_size):
        # Randomly move the human up to 4 spaces in any direction
        x, y = self.position
        new_x = random.randint(max(0, x - 4), min(map_size, x + 4))
        new_y = random.randint(max(0, y - 4), min(map_size, y + 4))
        self.position = (new_x, new_y)
        self.health -= 1
    def eat(self):
        if self.health < 100:
            self.health += 30
        if self.health > 100:
            self.health = 100
    def drink(self):
        if self.health < 100:
            self.health += 50
        if self.health > 100:
            self.health = 100   
    def eat_garlic(self):
        if self.health < 100:
            self.health =100
        
    def use_other(self, other):
        # One human uses the other, gaining 20 health while the other loses 20 health
        self.health += 20
        other.health -= 20
        if self.health > 100:
            self.health = 100

    def help_other(self, other):
        # Both humans help each other, gaining 10 health each
        self.health += 10
        other.health += 10
        if self.health > 100:
            self.health = 100

    def bitten(self):
        # The human gets bitten by a vampire and becomes a vampire
        self.health = 0
        
    def __str__(self):
        return f"Human: Health={self.health}, Age={self.age}, Position={self.position}"
