from collections import defaultdict

class Graph:
    def __init__(self):
        # graph[node][neighbor] = weight
        self.adjacency = defaultdict(dict)

    def add_edge(self, start, end, travel_time, delay):
        weight = travel_time + delay
        self.adjacency[start][end] = weight

    def get_neighbors(self, node):
        return self.adjacency.get(node, {})

    def __str__(self):
        return '\n'.join(f"{node} -> {neighbors}" for node, neighbors in self.adjacency.items())