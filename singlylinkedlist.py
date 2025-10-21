class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None # Reference to the next node

class SinglyLinkedList:
    """Manages the head of the linked list and provides core operations."""
    def __init__(self):
        self.head = None
        self._size = 0

    # -------------------------------------------------------------------
    # PUSH (Insert at Head) - O(1)
    # -------------------------------------------------------------------
    def push_front(self, data):
        """Adds a new node to the front (head) of the list."""
        new_node = Node(data)
        
        # 1. The new node's 'next' pointer points to the current head
        new_node.next = self.head
        
        # 2. Update the list's 'head' to be the new node
        self.head = new_node
        self._size += 1

    # -------------------------------------------------------------------
    # POP (Remove from Head) - O(1)
    # -------------------------------------------------------------------
    def pop_front(self):
        """Removes and returns the data from the head of the list."""
        if not self.head:
            return None # List is empty

        # 1. Store the head node temporarily
        popped_node = self.head
        
        # 2. Move the list's head pointer to the next node
        self.head = popped_node.next
        self._size -= 1
        
        # 3. Return the data of the popped node
        return popped_node.data

    # -------------------------------------------------------------------
    # TRAVERSAL & UTILITY METHODS
    # -------------------------------------------------------------------

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def __iter__(self):
        """Allows iteration (e.g., for node in list)"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        """Provides a string representation for easy printing."""
        return " -> ".join(map(str, self)) + " -> None"
