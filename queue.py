from collections import deque

# A Queue class built on top of deque
class Queue:
    def __init__(self):
        # Use a deque object as the internal storage
        self._items = deque()

    # Enqueue (Add element to the back)
    def enqueue(self, item):
        self._items.append(item)

    # Dequeue (Remove and return element from the front)
    def dequeue(self):
        if not self.is_empty():
            return self._items.popleft() # O(1)
        return None

    # Peek (View the front element)
    def peek(self):
        if not self.is_empty():
            return self._items[0]
        return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self._items) == 0

    # Get the size
    def size(self):
        return len(self._items)

# Example Usage
if __name__ == "__main__":
    q = Queue()
    print(f"Is empty? {q.is_empty()}") # Output: True

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(f"Size: {q.size()}")       # Output: 3
    print(f"Peek: {q.peek()}")       # Output: 10

    print(f"Dequeue: {q.dequeue()}") # Output: 10
    print(f"Dequeue: {q.dequeue()}") # Output: 20

    print(f"Size: {q.size()}")       # Output: 1
    print(f"Dequeue: {q.dequeue()}") # Output: 30
    print(f"Dequeue: {q.dequeue()}") # Output: None
