from collections import deque

class MyStack:

    def __init__(self):
        # We use a single deque to act as our FIFO queue 📥
        self.q = deque()

    def push(self, x: int) -> None:
        # 1. Add the new element to the back of the queue
        self.q.append(x)
        
        # 2. Rotate all existing elements behind 'x' to move 'x' to the front 🔄
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Since the newest element is always at the front, we pop from front 🔝
        return self.q.popleft()

    def top(self) -> int:
        # Return the element currently at the front without removing it 👀
        return self.q[0]

    def empty(self) -> bool:
        # Returns True if our queue is empty 🪹
        return len(self.q) == 0