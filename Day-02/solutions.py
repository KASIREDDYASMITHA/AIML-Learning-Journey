# ============================================================
# DSA DAY 02 - LOOPS
# ============================================================


# ============================================================
# Question 1: Find the factorial of a number using a while loop.
#
# Input: A positive integer N
# Output: Factorial of N
#
# Example:
# Input: 4
# Output: 24
# ============================================================

n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial:", fact)


# ============================================================
# Question 2: Find the factorial of a number using a for loop.
#
# Input: A positive integer N
# Output: Factorial of N
#
# Example:
# Input: 4
# Output: 24
# ============================================================

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)


# ============================================================
# Question 3: Find the sum of the digits of a number.
#
# Input: A positive integer N
# Output: Sum of all digits
#
# Example:
# Input: 4352
# Output: 14
# ============================================================

n = int(input("Enter a number: "))

s = 0

while n > 0:
    digit = n % 10
    s = s + digit
    n = n // 10

print("Sum of digits:", s)


# ============================================================
# Question 4: Find the sum of the first N natural numbers.
#
# Input: A positive integer N
# Output: Sum of numbers from 1 to N
#
# Example:
# Input: 5
# Output: 15
# ============================================================

n = int(input("Enter a number: "))

s = 0

for i in range(1, n + 1):
    s = s + i

print("Sum:", s)


# ============================================================
# Question 5: Count the number of digits in a number.
#
# Input: A positive integer N
# Output: Number of digits
#
# Example:
# Input: 1234
# Output: 4
# ============================================================

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)


# ============================================================
# Question 6: Find the digital sum of a number.
#
# Digital sum means repeatedly adding the digits until
# a single digit remains.
#
# Input: A positive integer N
# Output: Single digit
#
# Example:
# Input: 4352
# 4 + 3 + 5 + 2 = 14
# 1 + 4 = 5
# Output: 5
# ============================================================

n = int(input("Enter a number: "))

while n >= 10:

    s = 0

    while n > 0:
        digit = n % 10
        s = s + digit
        n = n // 10

    n = s

print("Digital Sum:", n)

# Question 7: Reverse a given number.
# Input: An integer n
# Output: The reversed number

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)