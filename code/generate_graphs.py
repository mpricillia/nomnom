import json
import matplotlib.pyplot as plt

with open('c:/Pythonn/FINAL_NLP/checkpoint-10000/trainer_state.json', 'r') as f:
    state = json.load(f)

log_history = state['log_history']

train_loss_steps = []
train_loss = []
eval_loss_steps = []
eval_loss = []
eval_acc_steps = []
eval_acc = []

for log in log_history:
    if 'loss' in log:
        train_loss_steps.append(log['step'])
        train_loss.append(log['loss'])
    if 'eval_loss' in log:
        eval_loss_steps.append(log['step'])
        eval_loss.append(log['eval_loss'])
    if 'eval_accuracy' in log:
        eval_acc_steps.append(log['step'])
        eval_acc.append(log['eval_accuracy'])

# Plot Loss
plt.figure(figsize=(10, 6))
plt.plot(train_loss_steps, train_loss, label='Training Loss', marker='o', color='blue')
if eval_loss:
    plt.plot(eval_loss_steps, eval_loss, label='Validation Loss', marker='o', color='orange')
plt.title('Training and Validation Loss')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.savefig('c:/Pythonn/FINAL_NLP/code/loss_graph.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot Accuracy
if eval_acc:
    plt.figure(figsize=(10, 6))
    plt.plot(eval_acc_steps, eval_acc, label='Validation Accuracy', marker='o', color='green')
    plt.title('Validation Accuracy')
    plt.xlabel('Steps')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.savefig('c:/Pythonn/FINAL_NLP/code/accuracy_graph.png', dpi=300, bbox_inches='tight')
    plt.close()
