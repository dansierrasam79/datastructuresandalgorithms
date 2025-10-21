from collections import defaultdict

class Graph:
    """
    A class to represent a graph data structure using an adjacency list.
    The graph can be directed or undirected, and edges can have weights.
    """

    def __init__(self, directed=False):
        """
        Initializes the graph.
        self.graph is a dictionary where keys are vertices and values are
        dictionaries of their neighbors {neighbor: weight}.
        """
        # Using defaultdict simplifies adding new vertices.
        self.graph = defaultdict(dict)
        self.directed = directed

    def add_edge(self, u, v, weight=1):
        """
        Adds an edge between vertex u and vertex v.

        Args:
            u: The source vertex.
            v: The destination vertex.
            weight (int, optional): The weight of the edge. Defaults to 1 for unweighted graphs.
        """
        # Add the edge from u to v
        self.graph[u][v] = weight

        # If the graph is undirected, add the reverse edge from v to u
        if not self.directed:
            self.graph[v][u] = weight

    def get_neighbors(self, vertex):
        """Returns the neighbors of a given vertex."""
        return self.graph.get(vertex, {})

    def get_vertices(self):
        """Returns a list of all vertices in the graph."""
        return list(self.graph.keys())

    def __str__(self):
        """Provides a user-friendly string representation of the graph."""
        if not self.graph:
            return "Graph is empty."

        representation = ""
        for u in self.graph:
            # For each vertex, list its neighbors and the edge weights
            neighbors = " -> ".join([f"{v}({w})" for v, w in self.graph[u].items()])
            representation += f"{u} -> {{{neighbors or ' '}}}\n"
        return representation

'''### How to Use It
Here’s a simple example demonstrating how to create and interact with the `Graph` class.

#### Example 1: Undirected & Unweighted Graph
Let's create a simple social network. '''

# 1. Create an undirected graph
social_network = Graph(directed=False)

# 2. Add edges (friendships)
social_network.add_edge("Alice", "Bob")
social_network.add_edge("Alice", "Carol")
social_network.add_edge("Bob", "David")
social_network.add_edge("Carol", "David")
social_network.add_edge("Eve", "Frank") # A separate group

# 3. Print the graph to see its structure
print("--- Social Network (Undirected) ---")
print(social_network)

# 4. Get specific information
print(f"Alice's friends: {social_network.get_neighbors('Alice').keys()}")
print(f"All people in the network: {social_network.get_vertices()}")

# 1. Create a directed graph
flight_routes = Graph(directed=True)

# 2. Add routes with costs (weights)
flight_routes.add_edge("New York", "London", weight=450)
flight_routes.add_edge("London", "Paris", weight=50)
flight_routes.add_edge("Paris", "Tokyo", weight=800)
flight_routes.add_edge("New York", "Tokyo", weight=1100) # Direct flight
flight_routes.add_edge("London", "New York", weight=430) # Return flight

# 3. Print the graph
print("\n--- Flight Routes (Directed & Weighted) ---")
print(flight_routes)

# 4. Get specific information
ny_destinations = flight_routes.get_neighbors("New York")
print(f"Flights from New York: {ny_destinations}")
print(f"Cost from New York to London: ${ny_destinations.get('London')}")
