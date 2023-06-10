from simulation import Simulation

import argparse

parser = argparse.ArgumentParser(
                    prog='Dummy ',
                    description='What the program does',
                    epilog='Text at the bottom of help')
parser.add_argument('--map_size', type=int, default=10, help='Size of the map')
parser.add_argument('--num_humans', type=int, default=5, help='Number of humans')
parser.add_argument('--num_vampires', type=int, default=5, help='Number of vampires')
parser.add_argument('--num_timesteps', type=int, default=10, help='Number of timesteps')
args = parser.parse_args()
if args.map_size < 0 or args.num_humans < 0 or args.num_vampires < 0 or args.num_timesteps < 0:
    print('Please enter a positive number')
    exit()
else:
    simulation=Simulation(args.map_size, args.num_humans, args.num_vampires, args.num_timesteps, 5, 5, 5)
    simulation.run_simulation()

# if __name__ == '__main__':
#     Run()      
# # # Set the parameters for the simulat
# # print('no of food', num_food,type(num_food))
# # # Create a simulation instance
# # simulation = Simulation( map_size, num_humans, num_vampires, num_timesteps, num_food, num_water, num_garlic)

# # Run the simulation
# # simulation.run_simulation()
