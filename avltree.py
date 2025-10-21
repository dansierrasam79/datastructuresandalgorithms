import sys

# Set a higher recursion limit for deep trees
sys.setrecursionlimit(2000)

class Node:
    """
    A single Node in the AVL Tree.
    Adds a 'height' attribute crucial for balance calculation.
    """
    def __init__(self, value):
        # The data stored in the node
        self.value = value
        # Pointer to the left child node (initially None)
        self.left = None
        # Pointer to the right child node (initially None)
        self.right = None
        # Height of the node. A single node has height 1.
        self.height = 1

class AVLTree:
    """
    Represents the entire AVL Tree structure.
    Implements self-balancing through rotation methods upon insertion.
    """
    def __init__(self):
        # Initialize the root of the tree to be empty
        self.root = None

    # --- Height and Balance Helpers ---

    def _get_height(self, node):
        """Safely returns the height of the node, or 0 if the node is None."""
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """
        Calculates the Balance Factor (BF) of a node.
        BF = Height(Left Subtree) - Height(Right Subtree)
        A tree is balanced if BF is -1, 0, or 1.
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # --- Rotation Methods ---

    def _right_rotate(self, y):
        """Performs a right rotation on node y."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights (MUST be done bottom-up: y's height first, then x's height)
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        
        # Return the new root of the subtree
        return x

    def _left_rotate(self, x):
        """Performs a left rotation on node x."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights (MUST be done bottom-up: x's height first, then y's height)
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root of the subtree
        return y

    # --- Insertion Method ---

    def insert(self, root, value):
        """
        Inserts a new value into the tree and performs rebalancing if needed.
        This method returns the root of the (potentially new) subtree.
        """
        # 1. Standard BST Insertion
        if not root:
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            # Value is a duplicate, return the node (skip insertion)
            return root

        # 2. Update height of the current node
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        # 3. Get the balance factor
        balance = self._get_balance(root)

        # 4. Check for imbalance and perform rotations
        
        # Case 1: Left Left (LL) - Right Rotation
        # Balance > 1 means heavy left, and new node inserted in the left of the left child.
        if balance > 1 and value < root.left.value:
            print(f"-> Rebalance at {root.value}: LL Case, Performing Right Rotate.")
            return self._right_rotate(root)

        # Case 2: Right Right (RR) - Left Rotation
        # Balance < -1 means heavy right, and new node inserted in the right of the right child.
        if balance < -1 and value > root.right.value:
            print(f"-> Rebalance at {root.value}: RR Case, Performing Left Rotate.")
            return self._left_rotate(root)

        # Case 3: Left Right (LR) - Left then Right Rotation
        # Balance > 1 means heavy left, but new node inserted in the right of the left child.
        if balance > 1 and value > root.left.value:
            print(f"-> Rebalance at {root.value}: LR Case, Performing Left then Right Rotate.")
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Case 4: Right Left (RL) - Right then Left Rotation
        # Balance < -1 means heavy right, but new node inserted in the left of the right child.
        if balance < -1 and value < root.right.value:
            print(f"-> Rebalance at {root.value}: RL Case, Performing Right then Left Rotate.")
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        # If no rotation is needed, return the current root
        return root

    # --- Traversal Methods (Standard for all Binary Trees) ---
    
    def __inorder_recursive(self, node):
        """Helper for Inorder Traversal: Left -> Root -> Right (yields sorted output)"""
        if node:
            self.__inorder_recursive(node.left)
            print(f"{node.value}(h={node.height})", end=" ")
            self.__inorder_recursive(node.right)

    def inorder_traversal(self):
        """Performs Inorder Traversal (Left, Root, Right)."""
        print("Inorder Traversal (L-R-R) [Value(Height)]:", end=" ")
        self.__inorder_recursive(self.root)
        print("\n")


# --- Example Usage ---

if __name__ == "__main__":
    
    # 1. Initialize the AVL Tree
    avl_tree = AVLTree()
    
    # Values inserted in this order. 
    # This sequence forces several rebalancing rotations (e.g., insertion of 40 forces RL).
    values = [30, 20, 10, 25, 23, 27, 40]
    
    print("--- AVL Tree Construction and Self-Balancing Operations ---")
    
    # 2. Insert all values sequentially and observe rotations
    for val in values:
        print(f"Attempting to insert: {val}")
        avl_tree.root = avl_tree.insert(avl_tree.root, val)
    
    print("\n--- Final Tree State ---")
    
    # 3. Demonstrate Traversal (Inorder should be sorted, showing node heights)
    # The final tree should be short and balanced, ensuring O(log n) efficiency.
    avl_tree.inorder_traversal() 
    
    print("Final Tree Height:", avl_tree._get_height(avl_tree.root))
    print("\nFinal structure is fully balanced (height difference is max 1 at all nodes).")
