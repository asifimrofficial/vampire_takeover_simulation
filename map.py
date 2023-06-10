import random

class Map:
    def __init__(self, size):
        self.size = size

    def generate_initial_positions(self, num_humans, num_vampires, num_food, num_water, num_garlic):
        positions = set()
        print('no of food', num_food,type(num_food))
        # Generate initial positions for humans
        while len(positions) < num_humans:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            positions.add((x, y))

        # Generate initial positions for vampires
        while len(positions) < num_humans + num_vampires:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            positions.add((x, y))

        # Generate initial positions for food
        food = []
        while len(food) < 4:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            position = (x, y)
            if position not in positions:
                food.append(position)

        # Generate initial positions for water
        water = []
        while len(water) < 5:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            position = (x, y)
            if position not in positions and position not in food:
                water.append(position)

        # Generate initial positions for garlic
        garlic = []
        while len(garlic) < 10:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            position = (x, y)
            if position not in positions and position not in food and position not in water:
                garlic.append(position)

        positions.update(food, water, garlic)

        return positions
