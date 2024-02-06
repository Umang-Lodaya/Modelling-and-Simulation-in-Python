from modsim import *
import matplotlib.pyplot as plt

# Create State of Bikes at both ends
bikeshare = State(olin = 10, wellesley = 2, olin_empty = 0, wellesley_empty = 0)
print(bikeshare)
print()

def bike_to_wellesley(state):
    """Move one bike from Olin to Wellesley.
    
    state: State object
    """
    if state.olin == 0:
        state.olin_empty += 1
        return
    state.olin -= 1
    state.wellesley += 1

def bike_to_olin(state):
    """Move one bike from Wellesley to Olin.
    
    state: State object
    """
    if state.wellesley == 0:
        state.wellesley_empty += 1
        return
    state.wellesley -= 1
    state.olin += 1

# Function to move bikes from each ends
def step(state, p1, p2):
    if flip(p1):
        bike_to_wellesley(state)
    if flip(p2):
        bike_to_olin(state)

def run_simulation(state, p1, p2, num_steps):
    """Simulate the given number of time steps.
    state: State object
    p1: probability of an Olin -> Wellesley customer arrival
    p2: probability of a Wellesley -> Olin customer arrival
    num_steps: number of time steps
    """
    results = TimeSeries()
    for i in range(num_steps):
        step(state, p1, p2)
        results[i] = state.olin

    # plt.plot(results)
    # plt.legend(["Olin"], loc = "best")
    # plt.show()

    # Getting mean value for number of bikes at one end
    print(results.mean())
    print()

run_simulation(bikeshare, 0.4, 0.2, 60)
print(bikeshare.olin_empty, bikeshare.wellesley_empty)