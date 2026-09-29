# DSA Day 30
# Maximum Rectangle in Skyline
# Approach 2: Left and Right Boundaries

# Input: Number of buildings
n = int(input("Enter number of buildings: "))

# Input: Heights of buildings
arr = list(map(int, input("Enter building heights: ").split()))

# Initialize maximum area
res = 0

# Traverse each building
for i in range(n):

    # Initialize left boundary
    left = -1

    # Find nearest smaller building on the left
    for j in range(i - 1, -1, -1):

        if arr[j] < arr[i]:
            left = j
            break

    # Initialize right boundary
    right = n

    # Find nearest smaller building on the right
    for j in range(i + 1, n):

        if arr[j] < arr[i]:
            right = j
            break

    # Calculate the width
    width = right - left - 1

    # Calculate the rectangular area
    area = arr[i] * width

    # Update maximum area
    res = max(res, area)

# Print the maximum rectangular area
print("Maximum rectangle area:", res)