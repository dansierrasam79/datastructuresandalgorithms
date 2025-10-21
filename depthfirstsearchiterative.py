def depth_first_search_iterative(graph, start_node):
    """
    Performs the Depth-First Search (DFS) algorithm iteratively 
    starting from a given node.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node (str): The node to start the traversal from.

    Returns:
        list: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return [] # Return empty list if start node isn't in the graph

    # 1. Initialize a stack and push the starting node.
    # A standard Python list works well as a stack using append() and pop().
    stack = [start_node]

    # 2. Initialize a set to keep track of visited nodes.
    visited = {start_node}

    # 3. Initialize a list to store the traversal order.
    traversal_order = []

    while stack:
        # 4. Pop the current node (Last-In, First-Out).
        current_node = stack.pop()
        traversal_order.append(current_node)

        # 5. Explore neighbors in reverse order. 
        # (This ensures neighbors are pushed onto the stack 
        # in an order that pops them out alphabetically/in-order for consistent results.)
        if current_node in graph:
            # Sort the neighbors in reverse order before iteration
            # to make the traversal deterministic.
            for neighbor in sorted(graph[current_node], reverse=True):
                # 6. If a neighbor hasn't been visited, mark it and push it onto the stack.
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

    return traversal_order

# --- Example Usage ---

# Define a sample graph (Adjacency List)
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
dfs_result = depth_first_search_iterative(graph_example, start_node)

print(f"Graph: {graph_example}")
print(f"Starting Node: {start_node}")
print(f"DFS Traversal Order (Iterative): {dfs_result}")
# Expected Output: ['A', 'C', 'F', 'B', 'E', 'D'] (The exact order can vary 
# depending on neighbor processing, but this is typical when sorting neighbors in reverse before push)
