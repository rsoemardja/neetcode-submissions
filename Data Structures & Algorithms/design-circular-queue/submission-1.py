class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initializes the object with the size of the queue to be k.
        """
        self.capacity = k
        self.queue = [0] * k  # Fixed-size buffer
        self.head = 0         # Points to the front element
        self.count = 0        # Current number of elements stored

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue.
        Returns True if successful, False if full.
        """
        if self.isFull():
            return False
        
        # Calculate insertion index: head + count wrapped around using capacity
        insert_idx = (self.head + self.count) % self.capacity
        self.queue[insert_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue.
        Returns True if successful, False if empty.
        """
        if self.isEmpty():
            return False
        
        # Advance head pointer forward with wrap-around
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Gets the front item from the queue.
        Returns -1 if empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Gets the last item from the queue.
        Returns -1 if empty.
        """
        if self.isEmpty():
            return -1
        # Calculate rear index using head offset
        rear_idx = (self.head + self.count - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full.
        """
        return self.count == self.capacity