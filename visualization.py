
import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, map_size):
        self.map_size = map_size
        self.fig, self.ax = plt.subplots()

    def update_plot(self, humans, vampires, food, water, garlic):
        # Clear the plot
        self.ax.clear()

        # Set plot limits based on map size
        self.ax.set_xlim(0, self.map_size)
        self.ax.set_ylim(0, self.map_size)

        # Plot humans
        for human in humans:
            self.ax.plot(human.position[0], human.position[1], 'go', markersize=5)

        # Plot vampires
        for vampire in vampires:
            self.ax.plot(vampire.position[0], vampire.position[1], color='red' ,marker='*', markersize=6)

        # Plot food, water, and garlic
        for f in food:
            self.ax.plot(f[0], f[1], 'd', color='brown', markersize=4)
        for w in water:
            self.ax.plot(w[0], w[1], 's', color='blue', markersize=4)
        for g in garlic:
            self.ax.plot(g[0], g[1], 'v', color='gray', markersize=4)

        # Add gridlines
        self.ax.grid(True)
    
        # Add title and labels
        self.ax.set_title("Vampire Takeover Simulation")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")

        # Pause to show the plot
        plt.pause(0.1)

    def show_plot(self):
        plt.show()
