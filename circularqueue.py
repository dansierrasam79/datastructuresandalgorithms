class CircularQueue:
    """
    A fixed-size Queue implemented using a list and modulo arithmetic.
    """
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        
        self.capacity = capacity
        # Initialize the list with None values
        self._items = [None] * capacity 
        
        self.front = 0  # Index of the first element (for dequeue)
        self.rear = 0   # Index where the next element will be inserted (for enqueue)
        self.size = 0   # Current number of elements in the queue

    # -------------------------------------------------------------------
    # ENQUEUE (O(1))
    # -------------------------------------------------------------------
    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return False

        # 1. Insert the item at the current rear index
        self._items[self.rear] = item
        
        # 2. Move the rear index forward, wrapping around if necessary
        self.rear = (self.rear + 1) % self.capacity
        
        # 3. Increment size
        self.size += 1
        print(f"Enqueued: {item}")
        return True

    # -------------------------------------------------------------------
    # DEQUEUE (O(1))
    # -------------------------------------------------------------------
    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None

        # 1. Retrieve the item at the current front index
        item = self._items[self.front]
        
        # Optional: Set the dequeued slot to None
        self._items[self.front] = None 

        # 2. Move the front index forward, wrapping around if necessary
        self.front = (self.front + 1) % self.capacity
        
        # 3. Decrement size
        self.size -= 1
        return item

    # -------------------------------------------------------------------
    # UTILITY METHODS
    # -------------------------------------------------------------------
    def peek(self):
        """Returns the front item without removing it."""
        if self.is_empty():
            return None
        return self._items[self.front]

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Checks if the queue is full."""
        # The queue is full when the current size equals the capacity
        return self.size == self.capacity

    def __len__(self):
        """Returns the current number of elements."""
        return self.size
    
    def display(self):
        """Prints the current state of the queue contents (only active items)."""
        if self.is_empty():
            print("Queue: []")
            return
            
        result = []
        for i in range(self.size):
            # Calculate the actual index in the list using front and modulo
            index = (self.front + i) % self.capacity
            result.append(self._items[index])
            
        print(f"Queue (Front->Rear): {result}")
