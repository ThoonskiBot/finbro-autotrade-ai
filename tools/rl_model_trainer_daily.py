from dqn_agent import DQNAgent
from finbro_rl_training_loop import build_replay_buffer
import os
import datetime
import torch

state_size = 3
action_size = 3
agent = DQNAgent(state_size, action_size)
buffer = build_replay_buffer()

# Train agent
for _ in range(10):
    agent.replay(batch_size=32)

# Save model
timestamp = datetime.datetime.now().strftime("%Y%m%d")
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, f"finbro_rl_model_{timestamp}.pt")
torch.save(agent.model.state_dict(), model_path)

# Save training log
log_path = f"reports/rl_training_log_{timestamp}.txt"
os.makedirs("reports", exist_ok=True)
with open(log_path, "w") as f:
    f.write(f"Model trained and saved to {model_path}\n")

print(f"✅ Model saved to {model_path}")
print(f"📝 Training log saved to {log_path}")
