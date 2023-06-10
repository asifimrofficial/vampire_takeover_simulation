from human import Human
from vampire import Vampire
from map import Map
import csv
from visualization import Visualization
import random
import os
class Simulation:
    def __init__(self, map_size, num_humans, num_vampires, num_timesteps, num_food, num_water, num_garlic):
        self.map_size = map_size
        self.num_humans = num_humans
        self.num_vampires = num_vampires
        self.num_food = num_food,
        self.num_water = num_water,
        self.num_garlic = num_garlic,
        self.num_timesteps = num_timesteps
        self.map = Map(self.map_size)
        self.humans = []
        self.vampires = []
        self.food = []
        self.water = []
        self.garlic = []
        self.eaten_humans=[]
        self.eaten_vampires=[]
        self.visualization = Visualization(self.map_size)
    def initialize_objects(self):
        print("Initializing objects...")
        # Generate initial positions for objects and instantiate humans, vampires, food, water, and garlic
        positions = self.map.generate_initial_positions(self.num_humans, self.num_vampires, self.num_food, self.num_water, self.num_garlic)
        # positions = self.map.generate_initial_positions(self.num_humans, self.num_vampires)
        print(positions)
        for i in range(self.num_humans):
            position = positions.pop()
            health = 100
            age = random.randint(10, 50)
            human = Human(health, age, position)
            self.humans.append(human)

        for i in range(self.num_vampires):
            position = positions.pop()
            health = random.randint(10, 100)
            vampire = Vampire(health, 0, position)
            self.vampires.append(vampire)

        for i in range(5):
            position = positions.pop()
            self.food.append(position)
        
        for i in range(5):
            position = positions.pop()
            self.water.append(position)
            
        for i in range(5):
            position = positions.pop()
            self.garlic.append(position)
    def move_objects(self):
        # Move humans and vampires randomly
        for human in self.humans:
            human.move(self.map_size)
        for vampire in self.vampires:
            vampire.move(self.map_size)
    def print_eaten(self):
        for human in self.eaten_humans:
            print('Eaten humans', human)
            print('-------------------')
        for vampire in self.eaten_vampires:
            print('Eaten vampires', vampire)
        print('---------TOTAL----------')
        print('no of humans', len(self.eaten_humans))
        print('no of vampires', len(self.eaten_vampires))    
    def interact(self):
        # Check for interactions between humans and vampires
        for human in self.humans:
            for vampire in self.vampires:
                if human.position == vampire.position:
                    if random.random() < 0.7:
                        # Human gets bitten
                        if human not in self.humans:
                            continue
                        self.eaten_humans.append(human)
                        self.humans.remove(human)
                        newvampire = Vampire(health=100, age=0, position=human.position)
                        self.vampires.append(newvampire)
                        print('new no of vampires', len(self.vampires))
                        vampire.bite()
                        print("A human was bitten by a vampire. at postion", human.position)
                        print(human)
                    else:
                        # Vampire gets killed by human
                        self.eaten_vampires.append(vampire)
                        self.vampires.remove(vampire)
                        print("A vampire was killed by a human. at postion", vampire.position)
                        print(vampire)

        # Check for interactions between humans
        for i in range(len(self.humans)):
            for j in range(i + 1, len(self.humans)):
                human1 = self.humans[i]
                human2 = self.humans[j]
                if human1.position == human2.position:
                    if random.random() < 0.4:
                        # One human uses the other
                        human1.use_other(human2)
                        print("One human used another. at postion", human1.position)
                    else:
                        # Both humans help each other
                        human1.help_other(human2)
                        print("Both humans helped each other. at postion", human1.position)
        # Check for interactions between vampires
        for i in range(len(self.vampires)):
            for j in range(i + 1, len(self.vampires)):
                vampire1 = self.vampires[i]
                vampire2 = self.vampires[j]
                if vampire1.position == vampire2.position:
                   vampire1.bite()
                   vampire2.bite()
                   print("Two vampires bit each other. at postion", vampire1.position)
                   
                        
        # Check for interactions between humans and food
        for human in self.humans:
            for food in self.food:
                if human.position == food:
                    human.eat()
                    self.food.remove(food)
                    print("A human ate food. at postion", human.position)
        # Check for interactions between humans and water
        for human in self.humans:
            for water in self.water:
                if human.position == water:
                    human.drink()
                    self.water.remove(water)
                    print('A human drank water. at postion',human.position,'with and now has health', human.health)
        # Check for interactions between humans and garlic
        for human in self.humans:
            for garlic in self.garlic:
                if human.position == garlic:
                    human.eat_garlic()
                    self.garlic.remove(garlic)
                    print("A human ate garlic. at postion", human.position)
    def writeCSV(filename,fields, rows):
        print('writing csv')
        try:
           
            with open ('simulation.csv', 'a') as csvfile:
                csvwriter = csv.writer(csvfile,lineterminator='\n')
                csvfile.seek(0, 2)
    
                if csvfile.tell() == 0:
                    csvwriter.writerow(fields)
                csvwriter.writerow(rows)
                
                
            print("CSV file created successfully")
        except IOError:
            print(IOError)
    def run_simulation(self):
        self.initialize_objects()
        self.visualization.update_plot(self.humans, self.vampires, self.food, self.water, self.garlic)
        print("Running simulation...")
        print('food', self.food)
        print('water', self.water)
        print('garlic', self.garlic)
       
       
        
        for timestep in range(self.num_timesteps):
            print('--------------------')
            print("Timestep:", timestep + 1)
            print('--------------------')
            self.move_objects()
            self.interact()
            self.visualization.update_plot(self.humans, self.vampires, self.food, self.water, self.garlic)
        print("Simulation finished.")
        print('---------Remaining-----------')
        print("Humans:")
        print(len(self.humans))
        print('--------------------')
        print("Vampires:")
        print(len(self.vampires))
        print('--------------------')
        print("Food:")
        print(len(self.food))
        print('--------------------')
        print("Water:")
        print(len(self.water))
        print('--------------------')
        print("Garlic:")
        print(len(self.garlic))
        
        print('---------Eaten-----------')
        self.print_eaten()
        self.visualization.show_plot()
        initial_vampires =self.num_vampires
        initial_humans = self.num_humans
        final_vampires = len(self.vampires)
        final_humans = len(self.humans)
         
        fields = ['initial_vampires', 'final_vampires',  'initial_humans','final_humans']
        rows=[initial_vampires, final_vampires, initial_humans, final_humans]
        
        self.writeCSV(fields, rows)
        # exit()
        
       
        
