# DSA Day 30
# Maximum Rectangle in Skyline
# Approach 1: Brute Force

# Input: Number of buildings
n = int(input("Enter number of buildings: "))

# Input: Heights of buildings
arr = list(map(int, input("Enter building heights: ").split()))

# Initialize maximum area
res = 0

# Traverse each building
for i in range(n):

    # Initialize minimum height
    min_height = arr[i]

    # Check consecutive buildings starting from i
    for j in range(i, n):

        # Find the minimum height
        min_height = min(min_height, arr[j])

        # Calculate the width
        width = j - i + 1

        # Calculate the rectangular area
        area = min_height * width

        # Update maximum area
        res = max(res, area)

# Print the maximum rectangular area
print("Maximum rectangle area:", res)