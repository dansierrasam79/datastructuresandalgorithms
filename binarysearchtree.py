class Node:
    """
    A single Node in the Binary Search Tree.
    Each node stores a comparable value and references to its left and right children.
    """
    def __init__(self, value):
        # The data stored in the node
        self.value = value
        # Pointer to the left child node (initially None)
        self.left = None
        # Pointer to the right child node (initially None)
        self.right = None

class BinarySearchTree:
    """
    Represents the entire Binary Search Tree structure, starting from the root node.
    Implements efficient insertion and search operations by maintaining the BST property.
    """
    def __init__(self):
        # Initialize the root of the tree to be empty
        self.root = None

    # --- Insertion Methods ---

    def insert(self, value):
        """Public method to insert a new value while maintaining the BST property."""
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_recursive(self.root, value)

    def __insert_recursive(self, current_node, value):
        """Helper for recursive insertion."""
        if value < current_node.value:
            # Go left
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.__insert_recursive(current_node.left, value)
        elif value > current_node.value:
            # Go right
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.__insert_recursive(current_node.right, value)
        # If value == current_node.value, we skip insertion (handling duplicates)

    # --- Search Methods ---

    def search(self, value):
        """
        Searches for a value in the tree.
        Returns the Node object if found, otherwise returns None.
        """
        return self.__search_recursive(self.root, value)

    def __search_recursive(self, current_node, value):
        """Helper for recursive searching."""
        if current_node is None or current_node.value == value:
            return current_node
        
        if value < current_node.value:
            # Search in the left subtree
            return self.__search_recursive(current_node.left, value)
        else:
            # Search in the right subtree
            return self.__search_recursive(current_node.right, value)

    # --- Traversal Methods (Standard for all Binary Trees) ---
    
    def __inorder_recursive(self, node):
        """Helper for Inorder Traversal: Left -> Root -> Right (yields sorted output in BST)"""
        if node:
            self.__inorder_recursive(node.left)
            print(f"{node.value}", end=" ")
            self.__inorder_recursive(node.right)

    def __preorder_recursive(self, node):
        """Helper for Preorder Traversal: Root -> Left -> Right"""
        if node:
            print(f"{node.value}", end=" ")
            self.__preorder_recursive(node.left)
            self.__preorder_recursive(node.right)

    def __postorder_recursive(self, node):
        """Helper for Postorder Traversal: Left -> Right -> Root"""
        if node:
            self.__postorder_recursive(node.left)
            self.__postorder_recursive(node.right)
            print(f"{node.value}", end=" ")

    def inorder_traversal(self):
        """Performs Inorder Traversal (Left, Root, Right)."""
        print("Inorder Traversal (L-R-R) [Sorted]:", end=" ")
        self.__inorder_recursive(self.root)
        print()

    def preorder_traversal(self):
        """Performs Preorder Traversal (Root, Left, Right)."""
        print("Preorder Traversal (R-L-R):", end=" ")
        self.__preorder_recursive(self.root)
        print()

    def postorder_traversal(self):
        """Performs Postorder Traversal (Left, Right, Root)."""
        print("Postorder Traversal (L-R-R):", end=" ")
        self.__postorder_recursive(self.root)
        print()

# --- Example Usage ---

if __name__ == "__main__":
    
    # 1. Initialize the Binary Search Tree
    bst = BinarySearchTree()
    
    # Values to insert (inserted in this order: 50, 30, 70, 20, 40, 60, 80)
    values = [50, 30, 70, 20, 40, 60, 80]
    
    print("--- Binary Search Tree Construction and Operations ---")
    print(f"Inserting values in order: {values}\n")

    # 2. Insert all values
    for val in values:
        bst.insert(val)

    # 3. Demonstrate Traversal (Inorder should be sorted)
    # Expected: 20 30 40 50 60 70 80
    bst.inorder_traversal() 
    
    # Expected: 50 30 20 40 70 60 80
    bst.preorder_traversal() 
    
    # Expected: 20 40 30 60 80 70 50
    bst.postorder_traversal()

    print("\n--- Search Operations ---")
    
    # 4. Demonstrate Searching
    search_value_found = 40
    search_value_not_found = 99
    
    result_found = bst.search(search_value_found)
    if result_found:
        print(f"Search for {search_value_found}: Found node with value {result_found.value}.")
    else:
        print(f"Search for {search_value_found}: Not Found.")

    result_not_found = bst.search(search_value_not_found)
    if result_not_found:
        print(f"Search for {search_value_not_found}: Found node with value {result_not_found.value}.")
    else:
        print(f"Search for {search_value_not_found}: Not Found.")
