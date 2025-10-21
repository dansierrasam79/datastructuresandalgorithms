import heapq

class PriorityQueue:
    """
    A Priority Queue implementation using Python's built-in heapq (min-heap).
    """
    def __init__(self):
        # The underlying list that stores the heap elements
        self._heap = [] 

    # Insertion (Enqueue)
    # The complexity is O(log n)
    def push(self, item):
        """Adds an item to the priority queue."""
        heapq.heappush(self._heap, item)

    # Deletion (Dequeue)
    # The complexity is O(log n)
    def pop(self):
        """Removes and returns the item with the highest priority (smallest value)."""
        if not self.is_empty():
            return heapq.heappop(self._heap)
        return None

    # Peek
    # The complexity is O(1)
    def peek(self):
        """Returns the item with the highest priority without removing it."""
        if not self.is_empty():
            return self._heap[0]
        return None

    def is_empty(self):
        return not self._heap

    def size(self):
        return len(self._heap)
