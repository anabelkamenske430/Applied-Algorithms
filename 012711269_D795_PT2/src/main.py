import os
import time
from data_loader import (
    load_ambulances,
    load_call_priorities,
    load_location_network,
    load_calls
)
from astar import find_fastest_path  #Import astar function
from dispatch import CallDispatcher

# Get the absolute path to the data folder
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, '..', 'data')

# Build full paths to each file
ambulance_path = os.path.join(data_dir, 'ambulance.csv')
priority_path = os.path.join(data_dir, 'call_priority.csv')
network_path = os.path.join(data_dir, 'location_network.csv')
calls_path = os.path.join(data_dir, 'calls.csv')

# Load data
ambulances = load_ambulances(ambulance_path)
priorities = load_call_priorities(priority_path)
graph = load_location_network(network_path)
calls = load_calls(calls_path)

# Test Graph
print("\n🗺️ Graph Sample:")
print(graph)
print("\n🔍 Neighbors of 'Intersection B':")
print(graph.get_neighbors('Intersection B'))

# Test Dijkstra's Algorithm
# Example: Find Fastest path from Ambulance 1 to first call
ambulance_location = ambulances['Ambulance 1']  # e.g., 'Intersection A'
call_location = calls[0]['Location']            # e.g., 'Intersection D'

print(f"\n🚨 Calculating route from {ambulance_location} to {call_location}...")
cost, path = find_fastest_path(graph, ambulance_location, call_location)

print("🛣️ Fastest Path:")
print(" → ".join(path))
print(f"🕒 Total Travel Cost: {cost}")

# Initialize dispatcher with calls and priority mapping
dispatch = CallDispatcher(calls, priorities, ambulances, graph)

# Simulate dispatching over time
print("\n🚦 Starting Dispatch Simulation...\n")

step = 1
timings = [] # To store calculation times
while dispatch.has_calls():
    print(f"⏱️ Step {step}")
    # Start the timing
    start_time = time.time()
    dispatch.dispatch_next_call()
    elapsed = time.time() - start_time
    timings.append(elapsed)

    print(f"⏱️ Route calculated in {elapsed:.6f} seconds\n")
    step += 1

print("\n✅ Simulation Complete. All calls dispatched.")

#report for average execution time
if timings:
    avg_time = sum(timings) / len(timings)
    print(f"\n📈 Average Route Calculation Time: {avg_time:.6f} seconds over {len(timings)} dispatches")
else:
    print("\n⚠️ No dispatches were timed.")
