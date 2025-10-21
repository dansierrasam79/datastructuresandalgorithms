from collections import deque

class Deque:
    """
    A Double-Ended Queue implementation using Python's collections.deque.
    """
    def __init__(self):
        # The internal storage is the deque object
        self._items = deque()

    # --- Front Operations ---

    # Push to Front (Add to the left/head)
    def push_front(self, item):
        self._items.appendleft(item) # O(1)

    # Pop from Front (Remove from the left/head)
    def pop_front(self):
        if not self.is_empty():
            return self._items.popleft() # O(1)
        return None
    
    # Peek Front
    def peek_front(self):
        if not self.is_empty():
            return self._items[0]
        return None

    # --- Back Operations ---

    # Push to Back (Add to the right/tail)
    def push_back(self, item):
        self._items.append(item) # O(1)

    # Pop from Back (Remove from the right/tail)
    def pop_back(self):
        if not self.is_empty():
            return self._items.pop() # O(1)
        return None

    # Peek Back
    def peek_back(self):
        if not self.is_empty():
            return self._items[-1]
        return None

    # --- Utility Methods ---

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
