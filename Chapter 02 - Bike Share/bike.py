from modsim import *
import matplotlib.pyplot as plt

# Create State of Bikes at both ends
bikeshare = State(olin = 10, wellesley = 2)
print(bikeshare)
print()

def bike_to_wellesley():
    print("Moving bike to Wellsley...")
    bikeshare.olin -= 1
    bikeshare.wellesley += 1

def bike_to_olin():
    print("Moving bike to Olin...")
    bikeshare.wellesley -= 1
    bikeshare.olin += 1

# Function to move bikes from each ends
def step(p1, p2):
    if flip(p1):
        bike_to_wellesley()
    if flip(p2):
        bike_to_olin()


# Creating Time Series to simulate movement of bikes
results = TimeSeries()
results[0] = bikeshare.olin

for i in range(10):
    step(0.3, 0.2)
    results[i] = bikeshare.olin

# Getting mean value for number of bikes at one end
print(results.mean())
print()

plt.plot(results, label = 'Olin')