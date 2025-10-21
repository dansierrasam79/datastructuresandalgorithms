class DisjointSet:
    """
    Implements the Disjoint Set Union (DSU) data structure
    with path compression and union by rank for efficiency.
    """
    def __init__(self, vertices):
        # Initialize each vertex as its own parent (representative)
        self.parent = list(range(vertices))
        # Initialize the rank (or height) of each tree to 0
        self.rank = [0] * vertices

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i.
        Uses Path Compression.
        """
        if self.parent[i] == i:
            return i
        # Path compression: make the current node's parent the root
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, u, v):
        """
        Unites the sets containing elements u and v.
        Uses Union by Rank.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Attach smaller rank tree under root of high rank tree
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            # If ranks are the same, make one the root and increment its rank
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True  # Union successful
        return False # Already in the same set (cycle detected)

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store edges (u, v, weight)

    def add_edge(self, u, v, w):
        """Adds an edge to the graph."""
        self.graph.append([u, v, w])

    def kruskal_mst(self):
        """
        Computes the Minimum Spanning Tree (MST) using Kruskal's algorithm.

        Returns:
            tuple: A tuple containing:
                   - mst_cost (int): The total weight of the MST.
                   - result (list): A list of edges in the MST: [[u, v, weight], ...]
        """
        result = []
        
        # 1. Sort all edges in non-decreasing order of their weight (the greedy step)
        self.graph.sort(key=lambda item: item[2])
        
        ds = DisjointSet(self.V)

        edge_index = 0  # Index to iterate through sorted edges
        mst_edges_count = 0  # Count of edges added to the MST

        # 2. Iterate through sorted edges until MST has V-1 edges
        while mst_edges_count < self.V - 1 and edge_index < len(self.graph):
            u, v, weight = self.graph[edge_index]
            edge_index += 1

            # Find the roots (representatives) of u and v
            root_u = ds.find(u)
            root_v = ds.find(v)

            # 3. Check for cycle: If the roots are different, adding the edge is safe
            if root_u != root_v:
                mst_edges_count += 1
                result.append([u, v, weight])
                
                # 4. Union the sets (merge the two trees)
                ds.union(u, v)

        # Calculate the total cost of the MST
        mst_cost = sum(edge[2] for edge in result)
        
        return mst_cost, result

# --- Example Usage ---

# Graph with 4 vertices (labeled 0, 1, 2, 3)
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

# Edges: (0, 3, 5), (0, 2, 6), (0, 1, 10), (1, 3, 15), (2, 3, 4)
# Sorted Edges: (2, 3, 4), (0, 3, 5), (0, 2, 6), (0, 1, 10), (1, 3, 15)

total_cost, mst = g.kruskal_mst()

print(f"Number of Vertices (V): {g.V}")
print(f"Graph Edges: {g.graph}")
print("\n--- Minimum Spanning Tree (MST) ---")
print(f"Edges in MST (u, v, weight): {mst}")
print(f"Total MST Cost: {total_cost}")

# Expected Output:
# Edges: [ [2, 3, 4], [0, 3, 5], [0, 1, 10] ]
# Total Cost: 4 + 5 + 10 = 19
