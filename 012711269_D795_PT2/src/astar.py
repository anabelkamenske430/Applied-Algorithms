import heapq

def heuristic(node, goal):
    # Simple heuristic: treat all nodes equally (can be replaced with real distance if available)
    return 0  # Replace with actual heuristic if coordinates are available

def find_fastest_path(graph, start, end):
    """
    A* Search Algorithm to find the fastest route from start to end.
    """
    queue = [(0, start, [start])]
    g_costs = {start: 0}
    visited = set()

    while queue:
        f_cost, current, path = heapq.heappop(queue)

        if current == end:
            return g_costs[current], path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph.get_neighbors(current).items():
            tentative_g = g_costs[current] + weight
            if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, end)
                heapq.heappush(queue, (f, neighbor, path + [neighbor]))

    return float('inf'), []