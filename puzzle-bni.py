import random

initial_state = ['C', 'A', ' ', 'B']
target = ['B', 'C', ' ', 'A']
initial_state_matriz = [[initial_state[0], initial_state[1]], [initial_state[2], initial_state[3]]]
target_state_matriz = [[target[0], target[1]], [target[2], target[3]]]

print(f"Initial State: {initial_state_matriz}")
print(f"Target: {target_state_matriz}")
random.shuffle(initial_state)

while(initial_state != target):
    random.shuffle(initial_state)
    initial_state_matriz = [[initial_state[0], initial_state[1]], [initial_state[2], initial_state[3]]]
    

print(f"Target found: {initial_state_matriz}")
