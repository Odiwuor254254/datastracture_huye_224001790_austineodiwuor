from collections import deque

# Step 1: Initialize the queue with 5 patients
# We'll name them Patient1 to Patient5
queue = deque([f"Patient{i}" for i in range(1, 6)])

# Step 2: Serve the first two patients
served_patients = []
for _ in range(2):
    served = queue.popleft()
    served_patients.append(served)
    print(f"Served: {served}")

# Step 3: Identify the second served patient
print(f"\nSecond patient served: {served_patients[1]}")