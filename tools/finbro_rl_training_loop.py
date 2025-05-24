from replay_buffer import ReplayBuffer
from dqn_agent import DQNAgent
import pandas as pd
import numpy as np
import os

LOG_PATH = "logs/trade_log.csv"
REWARD_COLUMN = "PnL"
STATE_FEATURES = ["feature1", "feature2", "feature3"]
ACTION_COLUMN = "action"

def extract_experience(row, next_row):
    state = row[STATE_FEATURES].values
    action = int(row[ACTION_COLUMN])
    reward = float(row[REWARD_COLUMN])
    next_state = next_row[STATE_FEATURES].values
    done = bool(next_row["done"]) if "done" in next_row else False
    return (state, action, reward, next_state, done)

def build_replay_buffer(log_path=LOG_PATH):
    df = pd.read_csv(log_path)
    buffer = ReplayBuffer(max_size=10000)
    for i in range(len(df) - 1):
        experience = extract_experience(df.iloc[i], df.iloc[i + 1])
        buffer.add(experience)
    print(f"✅ Replay buffer built: {buffer.size()} experiences loaded.")
    return buffer

if __name__ == "__main__":
    buffer = build_replay_buffer()
