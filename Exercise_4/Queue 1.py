from collections import deque

# Step 1: Initialize the queue with 12 clients
# Let's name them Client1 to Client12
queue = deque([f"Client{i}" for i in range(1, 13)])

# Step 2: Serve the first 7 clients
for _ in range(7):
    served = queue.popleft()
    print(f"Served: {served}")

# Step 3: Check who is now in front
if queue:
    print(f"\nClient now in front: {queue[0]}")
else:
    print("\nNo clients left in the queue.")