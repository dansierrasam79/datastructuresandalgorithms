class Node:
    """
    A single Node in the Binary Tree.
    Each node stores a value and references to its left and right children.
    """
    def __init__(self, value):
        # The data stored in the node
        self.value = value
        # Pointer to the left child node (initially None)
        self.left = None
        # Pointer to the right child node (initially None)
        self.right = None

class BinaryTree:
    """
    Represents the entire Binary Tree structure, starting from the root node.
    Provides methods for common tree operations like traversals.
    """
    def __init__(self, root_value=None):
        # Initialize the root of the tree
        self.root = Node(root_value) if root_value is not None else None

    # --- Private Recursive Traversal Methods ---
    
    def __inorder_recursive(self, node):
        """Helper for Inorder Traversal: Left -> Root -> Right"""
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

    # --- Public Traversal Methods ---

    def inorder_traversal(self):
        """Performs Inorder Traversal (Left, Root, Right) starting from the root."""
        print("Inorder Traversal (L-R-R):", end=" ")
        self.__inorder_recursive(self.root)
        print()

    def preorder_traversal(self):
        """Performs Preorder Traversal (Root, Left, Right) starting from the root."""
        print("Preorder Traversal (R-L-R):", end=" ")
        self.__preorder_recursive(self.root)
        print()

    def postorder_traversal(self):
        """Performs Postorder Traversal (Left, Right, Root) starting from the root."""
        print("Postorder Traversal (L-R-R):", end=" ")
        self.__postorder_recursive(self.root)
        print()

# --- Example Usage ---

if __name__ == "__main__":
    
    # 1. Create the Binary Tree structure using the Node class directly
    
    # Structure:
    #         10
    #        /  \
    #       5    15
    #      / \  / 
    #     2  7 12 
    
    # Create the root node
    root = Node(10)
    
    # Build the left subtree
    root.left = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(7)
    
    # Build the right subtree
    root.right = Node(15)
    root.right.left = Node(12)
    # root.right.right is None (optional)

    # 2. Initialize the BinaryTree class with the constructed root
    tree = BinaryTree()
    tree.root = root 

    print("--- Binary Tree Traversal Example ---")
    print("Tree structure values (top to bottom, left to right): 10, 5, 15, 2, 7, 12\n")

    # 3. Demonstrate Traversals
    
    # Expected: 2 5 7 10 12 15
    tree.inorder_traversal() 
    
    # Expected: 10 5 2 7 15 12
    tree.preorder_traversal() 
    
    # Expected: 2 7 5 12 15 10
    tree.postorder_traversal()
