class Node:
    """Represents a single node in the doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node
        self.prev = None  # Reference to the previous node

class DoublyLinkedList:
    """Manages the head and tail of the doubly linked list."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # -------------------------------------------------------------------
    # PUSH FRONT (O(1))
    # -------------------------------------------------------------------
    def push_front(self, data):
        """Adds a new node to the front (head) of the list."""
        new_node = Node(data)
        
        if self.head is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty
            new_node.next = self.head  # New node points to old head
            self.head.prev = new_node  # Old head points back to new node
            self.head = new_node       # Update list head
        
        self._size += 1

    # -------------------------------------------------------------------
    # POP FRONT (O(1))
    # -------------------------------------------------------------------
    def pop_front(self):
        """Removes and returns the data from the front (head) of the list."""
        if self.head is None:
            return None

        data = self.head.data
        
        if self.head == self.tail:
            # Only one node in the list
            self.head = None
            self.tail = None
        else:
            # Move head to the next node
            self.head = self.head.next
            self.head.prev = None  # New head's prev pointer is None
            
        self._size -= 1
        return data

    # -------------------------------------------------------------------
    # PUSH BACK (O(1))
    # -------------------------------------------------------------------
    def push_back(self, data):
        """Adds a new node to the back (tail) of the list."""
        new_node = Node(data)
        
        if self.tail is None:
            # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty
            new_node.prev = self.tail  # New node points back to old tail
            self.tail.next = new_node  # Old tail points to new node
            self.tail = new_node       # Update list tail
            
        self._size += 1

    # -------------------------------------------------------------------
    # POP BACK (O(1))
    # -------------------------------------------------------------------
    def pop_back(self):
        """Removes and returns the data from the back (tail) of the list."""
        if self.tail is None:
            return None

        data = self.tail.data
        
        if self.head == self.tail:
            # Only one node in the list
            self.head = None
            self.tail = None
        else:
            # Move tail to the previous node
            self.tail = self.tail.prev
            self.tail.next = None  # New tail's next pointer is None
            
        self._size -= 1
        return data

    # -------------------------------------------------------------------
    # TRAVERSAL & UTILITY
    # -------------------------------------------------------------------
    def size(self):
        return self._size

    def __iter__(self):
        """Allows iteration from head to tail."""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        """Provides a string representation."""
        return " <-> ".join(map(str, self))
