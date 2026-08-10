# DSA Day 02 - Pseudocode

## Question 1: Factorial of a Number Using While Loop

### Pseudocode

START

READ n

SET fact = 1
SET i = 1

WHILE i <= n

    fact = fact * i
    i = i + 1

END WHILE

PRINT fact

STOP


---

## Question 2: Factorial of a Number Using For Loop

### Pseudocode

START

READ n

SET fact = 1

FOR i FROM 1 TO n

    fact = fact * i

END FOR

PRINT fact

STOP


---

## Question 3: Sum of Digits

### Pseudocode

START

READ n

SET s = 0

WHILE n > 0

    digit = n MOD 10
    s = s + digit
    n = n DIV 10

END WHILE

PRINT s

STOP


---

## Question 4: Sum of First N Natural Numbers

### Pseudocode

START

READ n

SET s = 0

FOR i FROM 1 TO n

    s = s + i

END FOR

PRINT s

STOP
-----
## Question 5: Reverse a Number

### Pseudocode

START

READ n

SET rev = 0

WHILE n > 0

    digit = n MOD 10

    rev = rev * 10 + digit

    n = n DIV 10

END WHILE

PRINT rev

STOP