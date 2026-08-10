# DSA Day 02 - Loops and Basic Mathematical Problems

## Topics Covered

- Factorial of a number
- Factorial using while loop
- Factorial using for loop
- Sum of digits
- Sum of first N natural numbers
- Reverse a number
- while loop
- for loop
- Modulo operator (%)
- Integer division (//)
- Dry run and loop tracing

---

# 1. Factorial of a Number

The factorial of a non-negative integer n is the product of all positive integers from 1 to n.

## Formula

n! = n × (n-1) × (n-2) × ... × 1

## Example

5! = 5 × 4 × 3 × 2 × 1 = 120

## Important Case

0! = 1

## Approach

Initialize:

fact = 1

Then multiply fact by every number from 1 to n.

### Time Complexity

O(n)

### Space Complexity

O(1)

---

# 2. Factorial Using For Loop

The same factorial logic can be implemented using a for loop.

The loop iterates from 1 to n.

## Example

For n = 5:

1 × 2 × 3 × 4 × 5 = 120

### Time Complexity

O(n)

### Space Complexity

O(1)

---

# 3. Sum of Digits

The sum of digits is calculated by repeatedly extracting the last digit.

Two operators are important:

- `% 10` gives the last digit.
- `// 10` removes the last digit.

## Example

For n = 1234:

1234 % 10 = 4
1234 // 10 = 123

123 % 10 = 3
123 // 10 = 12

12 % 10 = 2
12 // 10 = 1

1 % 10 = 1
1 // 10 = 0

Therefore:

4 + 3 + 2 + 1 = 10

### Time Complexity

O(d), where d is the number of digits.

### Space Complexity

O(1)

---

# 4. Sum of First N Natural Numbers

The program adds all numbers from 1 to n.

## Example

For n = 5:

1 + 2 + 3 + 4 + 5 = 15

### Time Complexity

O(n)

### Space Complexity

O(1)

---

# 5. Reverse a Number

A number can be reversed by repeatedly extracting its last digit and adding it to the reversed number.

The main logic is:

```text
digit = n % 10
rev = rev * 10 + digit
n = n // 10