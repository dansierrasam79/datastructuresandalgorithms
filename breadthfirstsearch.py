from collections import deque

def breadth_first_search(graph, start_node):
    """
    Performs the Breadth-First Search (BFS) algorithm starting from a given node.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      e.g., {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], ...}
        start_node (str): The node to start the traversal from.

    Returns:
        list: A list of nodes in the order they were visited.
    """
    if start_node not in graph:
        return [] # Return empty list if start node isn't in the graph

    # 1. Initialize a queue and add the starting node.
    # deque is efficient for adding and removing from both ends (needed for a queue).
    queue = deque([start_node])

    # 2. Initialize a set to keep track of visited nodes.
    # Sets provide O(1) average time complexity for lookups/insertions.
    visited = {start_node}

    # 3. Initialize a list to store the traversal order.
    traversal_order = []

    while queue:
        # 4. Dequeue the current node.
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # 5. Explore neighbors.
        # Check if the current_node has any neighbors in the graph
        if current_node in graph:
            for neighbor in graph[current_node]:
                # 6. If a neighbor hasn't been visited, mark it as visited and enqueue it.
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

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
bfs_result = breadth_first_search(graph_example, start_node)

print(f"Graph: {graph_example}")
print(f"Starting Node: {start_node}")
print(f"BFS Traversal Order: {bfs_result}")
# Expected Output: ['A', 'B', 'C', 'D', 'E', 'F']
