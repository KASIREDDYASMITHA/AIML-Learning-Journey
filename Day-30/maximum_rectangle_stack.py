# DSA Day 30
# Maximum Rectangle in Skyline
# Approach 3: Optimized Stack Approach

# Input: Number of buildings
n = int(input("Enter number of buildings: "))

# Input: Heights of buildings
arr = list(map(int, input("Enter building heights: ").split()))

# Create an empty stack
stack = []

# Initialize maximum area
res = 0

# Traverse the buildings
for i in range(n + 1):

    # Pop elements while the current height is smaller
    while len(stack) > 0 and (i == n or arr[stack[-1]] > arr[i]):

        # Get the height of the popped building
        height = arr[stack.pop()]

        # Calculate the width
        if len(stack) == 0:
            width = i
        else:
            width = i - stack[-1] - 1

        # Calculate the rectangular area
        area = height * width

        # Update maximum area
        res = max(res, area)

    # Push only valid building indices
    if i < n:
        stack.append(i)

# Print the maximum rectangular area
print("Maximum rectangle area:", res)