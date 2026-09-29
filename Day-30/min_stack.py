# DSA Day 30
# Min Stack
# Push, Pop, Top and GetMin in O(1)

# Create an empty stack
stack = []

# Stores the current minimum element
minElement = 0

# Number of operations
n = int(input("Enter number of operations: "))

for i in range(n):

    # Enter operation
    operation = input("Enter operation: ").split()

    # PUSH
    if operation[0] == "push":

        # Get the value
        val = int(operation[1])

        # If stack is empty
        if len(stack) == 0:

            # Push the value
            stack.append(val)

            # First element becomes minimum
            minElement = val

        # If value is greater than or equal to minimum
        elif val >= minElement:

            # Push normally
            stack.append(val)

        # If value is smaller than current minimum
        else:

            # Store encoded value
            stack.append(2 * val - minElement)

            # Update minimum
            minElement = val

    # POP
    elif operation[0] == "pop":

        # Check whether stack is empty
        if len(stack) == 0:

            print("Stack is empty")

        else:

            # Remove the top element
            top = stack.pop()

            # If it is a normal value
            if top >= minElement:

                print("Popped:", top)

            # If it is an encoded value
            else:

                # Actual element being removed
                removedElement = minElement

                # Restore previous minimum
                minElement = 2 * minElement - top

                print("Popped:", removedElement)

    # TOP
    elif operation[0] == "top":

        # Check whether stack is empty
        if len(stack) == 0:

            print("Stack is empty")

        else:

            # Get the top value
            top = stack[-1]

            # If it is a normal value
            if top >= minElement:

                print("Top:", top)

            # If it is an encoded value
            else:

                print("Top:", minElement)

    # GET MINIMUM
    elif operation[0] == "getMin":

        # Check whether stack is empty
        if len(stack) == 0:

            print("Stack is empty")

        else:

            # Print the minimum element
            print("Minimum:", minElement)

    else:

        print("Invalid operation")