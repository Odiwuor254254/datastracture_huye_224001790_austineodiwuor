from collections import deque

# -------------------------------
# Airtel Rwanda: 12 clients queue
# -------------------------------
print(" Airtel Rwanda Queue Simulation")
airtel_queue = deque([f"Client{i}" for i in range(1, 13)])  # Clients 1 to 12

# Serve first 7 clients
for _ in range(7):
    served = airtel_queue.popleft()
    print(f"Served: {served}")

# Who is now in front?
print(f"Client now in front: {airtel_queue[0]}\n")  # Expected: Client8

# -------------------------------
# CHUK Rwanda: 5 patients queue
# -------------------------------
print(" CHUK Rwanda Queue Simulation")
chuk_queue = deque([f"Patient{i}" for i in range(1, 6)])  # Patients 1 to 5

# Serve first two patients
served_patients = []
for _ in range(2):
    served = chuk_queue.popleft()
    served_patients.append(served)
    print(f"Served: {served}")

# Who was second served?
print(f"Second patient served: {served_patients[1]}\n")  # Expected: Patient2

# -----------------------------------------
# Bank Counter: Compare Queue vs Stack
# -----------------------------------------
print(" Bank Counter Comparison")

# Queue Simulation (FIFO)
bank_queue = deque(["Customer1", "Customer2", "Customer3", "Customer4", "Customer5"])
print("\n Queue (FIFO):")
while bank_queue:
    current = bank_queue.popleft()
    print(f"Serving: {current}")

# Stack Simulation (LIFO)
bank_stack = ["Customer1", "Customer2", "Customer3", "Customer4", "Customer5"]
print("\n Stack (LIFO):")
while bank_stack:
    current = bank_stack.pop()
    print(f"Serving: {current}")

# -----------------------------------------
# Stack Challenge: Push, Pop, Push, Top
# -----------------------------------------
print("\n Stack Challenge Simulation")

# Step-by-step stack operations
stack = []

# Push A, B, C, D
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
print("Stack after pushing A, B, C, D:", stack)

# Pop 2 elements
stack.pop()  # Removes D
stack.pop()  # Removes C
print("Stack after popping 2 elements:", stack)

# Push E
stack.append("E")
print("Stack after pushing E:", stack)

# Check top
print(" Top of the stack:", stack[-1])  # Expected: E