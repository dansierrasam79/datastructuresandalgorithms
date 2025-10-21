import heapq

def prim_mst(graph, start_node):
    """
    Computes the Minimum Spanning Tree (MST) using Prim's algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Example: {'A': [('B', 2), ('C', 1)], ...}
        start_node (str): The node to start the MST construction from.

    Returns:
        tuple: A tuple containing:
               - mst_cost (int): The total weight of the MST.
               - mst_edges (list): A list of edges in the MST: [(u, v, weight), ...]
    """
    if start_node not in graph:
        return 0, []

    # Set to keep track of nodes already included in the MST
    visited = {start_node}

    # Priority Queue (Min-Heap): Stores edges as (weight, neighbor, current_node)
    # The current_node is the one already in the MST.
    pq = []
    
    # 1. Initialize the Priority Queue with all edges from the start_node
    # We add all the edges connected to the starting node to the heap.
    for neighbor, weight in graph.get(start_node, []):
        heapq.heappush(pq, (weight, start_node, neighbor))

    mst_cost = 0
    mst_edges = []

    # 2. Main Loop: Continue until all nodes are visited or the PQ is empty
    # For a connected graph, this loop runs V-1 times (where V is the number of vertices).
    while pq and len(visited) < len(graph):
        # Pop the edge with the minimum weight
        weight, u, v = heapq.heappop(pq)

        # 3. Check for cycles (by checking if the neighbor 'v' is already visited)
        if v in visited:
            continue  # Skip this edge, it would form a cycle

        # 4. Add the new node and edge to the MST
        visited.add(v)
        mst_cost += weight
        mst_edges.append((u, v, weight))

        # 5. Explore all edges connected to the newly added node 'v'
        # Add all new valid edges (connecting 'v' to an unvisited node) to the PQ
        for neighbor, new_weight in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(pq, (new_weight, v, neighbor))

    return mst_cost, mst_edges

# --- Example Usage ---

# Graph representation: Adjacency List with weights
graph_example = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 1)],
    'C': [('A', 3), ('B', 4), ('D', 5), ('E', 6)],
    'D': [('B', 1), ('C', 5), ('E', 7)],
    'E': [('C', 6), ('D', 7)]
}

start_node = 'A'
total_cost, mst = prim_mst(graph_example, start_node)

print(f"Graph: {graph_example}")
print(f"Starting Node: {start_node}")
print("\n--- Minimum Spanning Tree (MST) ---")
print(f"Total MST Cost: {total_cost}")
print(f"MST Edges (u, v, weight): {mst}")
# Expected MST Edges: [('A', 'B', 2), ('B', 'D', 1), ('A', 'C', 3), ('C', 'E', 6)]
# Total Cost: 2 + 1 + 3 + 6 = 12
