import csv
from graph import Graph

def load_ambulances(file_path):
    ambulances = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ambulances[row['Ambulance Number']] = row['Staging Location']
    return ambulances

def load_call_priorities(file_path):
    priorities = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            priorities[row['Call Type']] = int(row['Priority'])
    return priorities


def load_location_network(file_path):
    graph = Graph()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            start = row['Start']
            end = row['End']
            travel_time = float(row['Travel Time'])
            delay = float(row['Traffic Delay'])
            graph.add_edge(start, end, travel_time, delay)
    return graph

def load_calls(file_path):
    calls = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            calls.append({
                'Call ID': int(row['Call ID']),
                'Location': row['Location'],
                'Call Type': row['Call Type']
            })
    return calls
