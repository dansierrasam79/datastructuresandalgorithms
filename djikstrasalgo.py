import heapq

def dijkstra(graph, start_node):
    """
    Finds the shortest path distance from a start_node to all other nodes 
    in a graph with non-negative weights using Dijkstra's algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {'A': [('B', 2), ('C', 1)], 'B': [('D', 1)], ...}
        start_node (str): The node to start the shortest path calculation from.

    Returns:
        dict: A dictionary containing the shortest distance from the start_node 
              to every reachable node.
        dict: A dictionary storing the predecessor of each node on the shortest path.
    """
    if start_node not in graph:
        print(f"Error: Start node '{start_node}' not found in graph.")
        return {}, {}

    # 1. Initialize distances and setup the priority queue
    
    # Distance map: Stores the shortest distance from start_node to each node.
    # Initialize all distances to infinity, except for the start node (distance 0).
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    
    # Predecessor map: Stores the optimal preceding node on the shortest path.
    predecessors = {node: None for node in graph}

    # Priority Queue (Min-Heap): Stores elements as (distance, node)
    # Start with the initial node.
    priority_queue = [(0, start_node)]

    # 2. Main loop: Process nodes in order of increasing distance
    while priority_queue:
        # Extract the node 'u' with the minimum distance 'd' from the priority queue
        current_distance, u = heapq.heappop(priority_queue)

        # Optimization: If the extracted distance is greater than the best known 
        # distance, skip processing (it's an outdated entry).
        if current_distance > distances[u]:
            continue

        # 3. Explore neighbors of the current node 'u'
        for v, weight in graph.get(u, []):
            # Calculate the distance to the neighbor 'v' through 'u'
            distance_through_u = current_distance + weight

            # 4. Relaxation Step: Check if this new path is shorter
            if distance_through_u < distances[v]:
                # Update distance and predecessor
                distances[v] = distance_through_u
                predecessors[v] = u
                
                # Push the updated distance to the priority queue
                # This automatically handles the "set of unvisited nodes" concept
                heapq.heappush(priority_queue, (distance_through_u, v))

    return distances, predecessors

# --- Example Usage ---

# Graph representation: Nodes are strings, weights are positive integers.
graph_example = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 1), ('E', 5)],
    'C': [('D', 3), ('E', 9)],
    'D': [('F', 2)],
    'E': [('F', 4)],
    'F': [] # Terminal node
}

start_node = 'A'
shortest_distances, path_predecessors = dijkstra(graph_example, start_node)

print(f"Graph Structure: {graph_example}")
print(f"Starting Node: {start_node}")

print("\n--- Shortest Distances from Start Node ---")
for node, distance in shortest_distances.items():
    # Only print reachable nodes (non-infinity)
    if distance != float('inf'):
        print(f"Shortest distance to {node}: {distance}")

print("\n--- Shortest Path Predecessors ---")
print(path_predecessors)

# Example to reconstruct the path to 'F'
def reconstruct_path(predecessors, end_node):
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    return " -> ".join(path[::-1])

end_node = 'F'
path_to_f = reconstruct_path(path_predecessors, end_node)
print(f"\nShortest Path to {end_node}: {path_to_f}")
