from modsim import *
import matplotlib.pyplot as plt
from numpy import linspace

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

def run_simulation(p1, p2, num_steps):
    state = State(olin=10, wellesley=2,olin_empty=0, wellesley_empty=0)
    for i in range(num_steps):
        step(state, p1, p2)
    
    return state
    
sweep = SweepSeries()
p1_array = linspace(0, 1, 5)
p2 = 0.2
num_steps = 60

for p1 in p1_array:
    state = run_simulation(p1, p2, num_steps)
    sweep[p1] = state.olin_empty

plt.plot(sweep)
plt.show()