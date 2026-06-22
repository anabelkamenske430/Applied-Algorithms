import heapq

def find_shortest_path(graph, start, end):
    """
    Uses Dijkstra's algorithm to find the shortest path from start to end.

    Parameters:
    - graph: instance of Graph class
    - start: starting node (string)
    - end: destination node (string)

    Returns:
    - (total_cost, path): tuple of shortest cost and list of nodes in path
    """
    # Priority queue: (cost_so_far, current_node, path_so_far)
    queue = [(0, start, [start])]
    visited = {}

    while queue:
        cost, node, path = heapq.heappop(queue)

        # Skip if we've already found a better path
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        # Destination reached
        if node == end:
            return cost, path

        # Explore neighbors
        for neighbor, weight in graph.get_neighbors(node).items():
            total_cost = cost + weight
            heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    # No path found
    return float('inf'), []