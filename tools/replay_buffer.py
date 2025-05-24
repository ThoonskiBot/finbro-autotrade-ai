import random
from collections import deque

class ReplayBuffer:
    def __init__(self, max_size=10000):
        self.buffer = deque(maxlen=max_size)

    def add(self, experience):
        self.buffer.append(experience)

    def sample(self, batch_size=64):
        return random.sample(self.buffer, min(len(self.buffer), batch_size))

    def size(self):
        return len(self.buffer)
