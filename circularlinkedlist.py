class Node:
    """Represents a single node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None # Will point to another Node

class CircularList:
    """Manages the circular linked list structure, tracking the tail."""
    def __init__(self):
        self.tail = None
        self._size = 0

    # -------------------------------------------------------------------
    # UTILITY METHODS
    # -------------------------------------------------------------------

    def is_empty(self):
        return self.tail is None

    def size(self):
        return self._size

    def peek_front(self):
        """Returns the data of the head node without removing it."""
        if self.is_empty():
            return None
        # Head is always the node following the tail
        return self.tail.next.data
        
    # -------------------------------------------------------------------
    # PUSH FRONT (O(1))
    # -------------------------------------------------------------------
    def push_front(self, data):
        """Adds a new node to the front (head) of the list."""
        new_node = Node(data)
        
        if self.is_empty():
            # If empty, the new node is both the head and the tail, 
            # and it points to itself.
            new_node.next = new_node
            self.tail = new_node
        else:
            # 1. New node points to the current head
            current_head = self.tail.next
            new_node.next = current_head
            
            # 2. The tail points to the new node, making it the new head
            self.tail.next = new_node
        
        self._size += 1

    # -------------------------------------------------------------------
    # POP FRONT (O(1))
    # -------------------------------------------------------------------
    def pop_front(self):
        """Removes and returns the data from the front (head) of the list."""
        if self.is_empty():
            return None

        # 1. Get a reference to the head node
        head_node = self.tail.next
        data = head_node.data
        
        if head_node == self.tail:
            # Only one node in the list
            self.tail = None
        else:
            # 2. Make the tail skip the head node (tail points to head's next)
            self.tail.next = head_node.next
        
        self._size -= 1
        return data

    # -------------------------------------------------------------------
    # PUSH BACK (O(1))
    # -------------------------------------------------------------------
    def push_back(self, data):
        """Adds a new node to the back (tail) of the list."""
        # Due to the circular nature, this operation is identical to push_front, 
        # except we update the tail pointer at the end.
        self.push_front(data)
        
        # The node we just added is now the head, so we make it the new tail.
        # This shifts the tail pointer one spot forward.
        self.tail = self.tail.next
        
    # -------------------------------------------------------------------
    # TRAVERSAL & DISPLAY
    # -------------------------------------------------------------------
    def __repr__(self):
        """Provides a string representation for easy printing."""
        if self.is_empty():
            return "CircularList: []"

        current = self.tail.next  # Start at the head
        parts = []
        
        # Iterate until we get back to the head node
        while current is not self.tail:
            parts.append(str(current.data))
            current = current.next
        
        # Add the tail node's data
        parts.append(str(self.tail.data))

        return "CircularList: " + " -> ".join(parts) + " -> (Head)"
