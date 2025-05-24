import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np

class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        return self.fc2(x)

class DQNAgent:
    def __init__(self, state_size, action_size, lr=0.001, gamma=0.99):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = gamma
        self.model = DQN(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, epsilon=0.1):
        if random.random() <= epsilon:
            return random.randint(0, self.action_size - 1)
        with torch.no_grad():
            state = torch.FloatTensor(state)
            q_values = self.model(state)
            return q_values.argmax().item()

    def replay(self, batch_size=32):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state = torch.FloatTensor(next_state)
                target += self.gamma * torch.max(self.model(next_state)).item()
            state = torch.FloatTensor(state)
            output = self.model(state)[action]
            loss = self.criterion(output, torch.tensor(target))
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
