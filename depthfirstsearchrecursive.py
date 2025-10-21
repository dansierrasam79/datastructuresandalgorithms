def depth_first_search_recursive(graph, current_node, visited=None, traversal_order=None):
    """
    Performs the Depth-First Search (DFS) algorithm recursively.

    Note: This is a common pattern for recursive graph traversal, 
    using optional parameters for shared state (visited set and traversal list).
    """
    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []
        
    # Base case for recursion: if node is not in graph
    if current_node not in graph and current_node not in visited:
        return traversal_order

    # 1. Mark the current node as visited and record it.
    visited.add(current_node)
    traversal_order.append(current_node)

    # 2. Explore neighbors.
    if current_node in graph:
        # Sort neighbors for deterministic traversal result
        for neighbor in sorted(graph[current_node]):
            # 3. If a neighbor hasn't been visited, recurse on it.
            if neighbor not in visited:
                depth_first_search_recursive(graph, neighbor, visited, traversal_order)

    return traversal_order

# --- Example Usage (Recursive) ---
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start_node = 'A'
dfs_recursive_result = depth_first_search_recursive(graph_example, start_node)

print(f"\nDFS Traversal Order (Recursive): {dfs_recursive_result}")
# Expected Output: ['A', 'B', 'D', 'E', 'F', 'C'] 
# (This order differs from the iterative one because of neighbor sorting order)
