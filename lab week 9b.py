import random

class Agent:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
    
    def find_empty_patch(self):
        # Find an empty patch in the world
        empty_patches = self.world.get_empty_patches()
        if empty_patches:
            return random.choice(empty_patches)
        else:
            return None
    
    def move(self, new_patch):
        # Move the agent to a new patch
        self.world.grid[self.y][self.x] = 0
        self.x, self.y = new_patch
        self.world.grid[self.y][self.x] = 1

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialize the grid with all patches empty (0)
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.agents = []
    
    def add_agent(self, agent):
        # Add an agent to the world
        self.agents.append(agent)
        self.grid[agent.y][agent.x] = 1
    
    def get_empty_patches(self):
        # Return a list of empty patches in the world
        empty_patches = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 0:
                    empty_patches.append((x, y))
        return empty_patches
    
    def simulate(self, steps):
        # Simulate the world for a given number of steps
        for _ in range(steps):
            for agent in self.agents:
                new_patch = agent.find_empty_patch()
                if new_patch:
                    agent.move(new_patch)
    
    def print_grid(self):
        # Print the current state of the grid
        for row in self.grid:
            print(row)

# Initialize the world
width, height = 5, 5
num_agents = 3
steps = 10

world = World(width, height)

# Add agents to the world
for _ in range(num_agents):
    x, y = random.choice(world.get_empty_patches())
    agent = Agent(world, x, y)
    world.add_agent(agent)

# Print the initial state of the grid
print("Initial grid:")
world.print_grid()

# Simulate the world for a given number of steps
world.simulate(steps)

# Print the final state of the grid
print(f"\nGrid after {steps} steps:")
world.print_grid()


