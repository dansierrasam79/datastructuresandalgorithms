class BTreeNode:
    """
    Represents a single node in the B-Tree.
    A node stores a list of keys, and if it's not a leaf, a list of child pointers.
    """
    def __init__(self, t, is_leaf):
        # Minimum degree (t). Defines the capacity constraints.
        self.t = t
        # List of keys stored in the node. Max size is 2*t - 1.
        self.keys = []
        # List of child nodes. Max size is 2*t. Only used if not a leaf.
        self.children = []
        # Boolean, true if the node is a leaf (has no children).
        self.is_leaf = is_leaf

class BTree:
    """
    Represents the B-Tree structure.
    Implements search and the complex insertion logic involving node splitting.
    """
    def __init__(self, t=3):
        # Minimum degree t. (e.g., t=3 means max 5 keys, max 6 children per node)
        self.t = t
        # Root is initially None
        self.root = None
        # Root height is always 1 when initialized
        self.root = BTreeNode(t, True)

    # --- Search Operation ---

    def search(self, k, node=None):
        """
        Public method to search for key k starting from the root.
        Returns the (node, index) tuple where the key is found, or None.
        """
        if node is None:
            node = self.root
            
        i = 0
        # Find the smallest index i such that k <= node.keys[i]
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        # Check if the key is found at index i
        if i < len(node.keys) and k == node.keys[i]:
            return (node, i)

        # If it's a leaf and not found, the key is not in the tree
        if node.is_leaf:
            return None
        else:
            # Recurse into the appropriate child
            return self.search(k, node.children[i])

    # --- Insertion Operation ---

    def insert(self, k):
        """
        Inserts a new key k into the B-Tree.
        Handles the case where the root needs to be split.
        """
        r = self.root
        # Check if the root is full (2*t - 1 keys)
        if len(r.keys) == (2 * self.t) - 1:
            # Tree grows in height: create a new root
            s = BTreeNode(self.t, False)
            s.children.insert(0, r)
            self._split_child(s, 0, r)
            
            # The new root becomes 's'
            self.root = s
            self._insert_non_full(s, k)
        else:
            # Root is not full, proceed with standard insertion
            self._insert_non_full(r, k)

    def _insert_non_full(self, x, k):
        """
        Helper method to insert key k into a non-full node x.
        If a child is full, it is split first.
        """
        i = len(x.keys) - 1
        
        if x.is_leaf:
            # If it's a leaf, insert the key directly
            x.keys.append(0) # Make space
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
            
        else:
            # Find the child where k should be inserted
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1 # i is the index of the child pointer

            # If the chosen child is full, split it
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i, x.children[i])
                
                # After splitting, x.keys[i] contains the median. 
                # Determine which of the two new children k belongs to.
                if k > x.keys[i]:
                    i += 1
            
            # Recurse into the appropriate (now non-full) child
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i, y):
        """
        Splits the full child y of node x at index i.
        The median key of y is promoted to x.
        A new node z is created to hold the upper half of y's keys and children.
        """
        t = self.t
        # Create new node z to store the upper half of y's data
        z = BTreeNode(t, y.is_leaf)
        
        # 1. Promote median key y.keys[t-1] to x.
        x.keys.insert(i, y.keys[t - 1])
        
        # 2. Insert new child z into x's children list
        x.children.insert(i + 1, z)
        
        # 3. Move the upper half of keys from y to z
        z.keys = y.keys[t:]
        
        # 4. Trim the keys list of y (keep only the lower half)
        y.keys = y.keys[:t - 1] 

        # 5. If y is not a leaf, move the upper half of children from y to z
        if not y.is_leaf:
            z.children = y.children[t:]
            # 6. Trim the children list of y (keep only the lower half)
            y.children = y.children[:t]

    # --- Traversal/Visualization (Simplified Preorder for Demonstration) ---
    
    def _print_tree(self, node, level=0):
        """Helper to print the tree structure."""
        if not node:
            return

        # Print keys of the current node
        indent = "  " * level
        print(f"{indent}Level {level}: {node.keys}")

        # Recurse through children
        if not node.is_leaf:
            for child in node.children:
                self._print_tree(child, level + 1)
        
    def print_tree(self):
        """Prints the structure of the entire B-Tree."""
        print("--- B-Tree Structure (t={}) ---".format(self.t))
        self._print_tree(self.root)
        print("---------------------------------")


# --- Example Usage ---

if __name__ == "__main__":
    
    # 1. Initialize a B-Tree with t=3 (Max keys per node = 5)
    b_tree = BTree(t=3)
    
    # Values inserted sequentially to demonstrate splitting and height growth
    values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35, 45, 55]
    
    print("B-Tree initialized with t=3.")
    print(f"Insertion sequence: {values}\n")

    # 2. Insert all values
    for i, val in enumerate(values):
        b_tree.insert(val)
        if i == 5:
            # Show the state after the first split (60 splits the root 30, 40, 50)
            print(">>> Tree state after inserting 60 (Root Split):")
            b_tree.print_tree()
    
    # 3. Print the final tree structure
    print("\n>>> Final B-Tree Structure:")
    b_tree.print_tree()
    
    # 4. Demonstrate Search Operations
    print("\n--- Search Operations ---")
    
    search_key_found = 45
    search_key_not_found = 99
    
    result_found = b_tree.search(search_key_found)
    if result_found:
        node, index = result_found
        print(f"Search for {search_key_found}: Found in node keys {node.keys} at index {index}.")
    else:
        print(f"Search for {search_key_found}: Not Found.")

    result_not_found = b_tree.search(search_key_not_found)
    if result_not_found:
        node, index = result_not_found
        print(f"Search for {search_key_not_found}: Found in node keys {node.keys} at index {index}.")
    else:
        print(f"Search for {search_key_not_found}: Not Found.")
