# Stack simulation for UR quizzes
stack = []

# Push operations
stack.append("Quiz1")
stack.append("Quiz2")
stack.append("Quiz3")

# Undo one (Pop)
stack.pop()

# Check top of stack
top_item = stack[-1]
print("Top of stack after undo:", top_item)