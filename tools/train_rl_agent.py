from dqn_agent import DQNAgent
from replay_buffer import ReplayBuffer
import numpy as np

# Dummy environment interaction loop
state_size = 10
action_size = 3
agent = DQNAgent(state_size, action_size)
buffer = ReplayBuffer()

# Simulate some training episodes
for episode in range(10):
    state = np.random.rand(state_size)
    for t in range(50):
        action = agent.act(state)
        next_state = np.random.rand(state_size)
        reward = np.random.randn()
        done = (t == 49)
        buffer.add((state, action, reward, next_state, done))
        state = next_state
    # Train the agent after each episode
    for _ in range(5):
        agent.replay(batch_size=16)

print("✅ Agent training complete.")
