# Day 14 - KNN Distance Functions

# ---------------------------------------
# Euclidean Distance
# ---------------------------------------

def euclidean(row1, row2):
    x1 = row1[0]
    y1 = row1[1]

    x2 = row2[0]
    y2 = row2[1]

    squared_distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

    euclidean_distance = squared_distance ** 0.5

    return euclidean_distance


# ---------------------------------------
# Manhattan Distance
# ---------------------------------------

def manhattan(row1, row2):
    x1 = row1[0]
    y1 = row1[1]

    x2 = row2[0]
    y2 = row2[1]

    manhattan_distance = abs(x1 - x2) + abs(y1 - y2)

    return manhattan_distance


# ---------------------------------------
# Dataset
# ---------------------------------------

# Red --> 0
# Blue --> 1

dataset = [
    [1, 2, 0],  # A
    [2, 3, 0],  # B
    [3, 2, 0],  # C
    [6, 5, 1],  # D
    [7, 4, 1],  # E
    [6, 6, 1]   # F
]


# ---------------------------------------
# Get Neighbours
# ---------------------------------------

def get_neighbours(dataset, pred_row, k):
    distances = []

    return distances


# ---------------------------------------
# Testing
# ---------------------------------------

print("Euclidean Distance:")
print(euclidean([1, 2], [2, 3]))

print()

print("Manhattan Distance:")
print(manhattan([1, 2], [2, 3]))