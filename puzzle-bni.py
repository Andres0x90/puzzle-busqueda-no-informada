import random

initial_state = [7,2,4,5,0,6,8,3,1]
target = [0,1,2,3,4,5,6,7,8]

print(f"Initial State: {initial_state}")
print(f"Target: {target}")

while(initial_state != target):
    random.shuffle(initial_state)

print(f"Target found: {initial_state}")
