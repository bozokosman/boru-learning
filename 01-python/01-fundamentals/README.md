🇹🇷 [Türkçe](README.tr.md)

# Python Fundamentals

This section contains the fundamental building blocks of the Python learning path.

The goal is not merely to memorize Python syntax, but to be able to write small programs by utilizing variables, data types, user inputs, operators, conditionals, loops, and basic string operations.

---

## Topics

### 01. Variables
Creating variables, assigning values, and changing their values.

Key concepts learned:
- Variable declaration
- Assignment
- Reassignment
- Variable naming
- Working with multiple variables
- Using f-strings

**Example:**
```python
name = "Osman"
age = 32

print(f"My name is {name}. I am {age} years old.")
```

### 02. Data Types
Basic data types in Python.

Key types learned:
- `str`
- `int`
- `float`
- `bool`
- `list`
- `tuple`
- `dict`
- `None`

Additionally, `type()` was used to check the data type of a variable.

### 03. Input / Output
Taking data from the user and generating program output.

Key concepts learned:
- `input()`
- `print()`
- `sep`
- `end`
- f-strings

**Example:**
```python
name = input("Enter your name: ")

print(f"Hello, {name}.")
```

### 04. Type Conversion
Converting data from one type to another.

Basic conversion functions:
- `int()`
- `float()`
- `str()`
- `bool()`

Specifically learned that the `input()` function always returns a `str` and proper type conversion is required for mathematical operations.

**Example:**
```python
age = int(input("Enter your age: "))

print(age + 5)
```
Also tested that in `bool()` conversion, the value 0 is `False`, while non-zero numbers are `True`.

### 05. Operators
Basic operators in Python.

**Arithmetic Operators**
- `+`
- `-`
- `*`
- `/`
- `//`
- `%`
- `**`

**Comparison Operators**
- `>`
- `<`
- `>=`
- `<=`
- `==`
- `!=`

**Logical Operators**
- `and`
- `or`
- `not`

Also studied operator precedence and how the use of parentheses changes the outcome of operations.

### 06. Conditionals
Using conditional statements to make the program behave differently based on specific conditions.

Basic structures:
- `if`
- `elif`
- `else`

Key concepts learned:
- Single condition
- Multiple conditions
- Nested conditions
- `and`
- `or`
- `not`
- Boolean expressions
- Conditional program flow

**Example:**
```python
if age >= 18:
    print("You can log in.")
else:
    print("You cannot log in.")
```

### 07. Loops
Using loops to allow the code to perform specific operations repeatedly.

Structures learned:
- `for`
- `while`
- `range()`
- `break`
- `for` with `else`
- Conditional loops

**Example:**
```python
for i in range(1, 11):
    print(i)
```
Also practiced iterating over lists and using conditions inside loops.

### 08. Strings
Studied the string data type and basic string operations.

Methods and operations learned:
- Indexing
- Slicing
- `strip()`
- `lower()`
- `upper()`
- `capitalize()`
- `replace()`
- `split()`
- `join()`
- `in`
- `for` loop over a string
- f-strings

**Example:**
```python
book = "  Python101  "

book = book.strip().lower()

print(book)
```
Also used `split()` for string → list conversion and `join()` for list → string conversion.

---

## Learning Structure
Each topic is archived in three sections:

```text
Topic
├── Notes
├── Examples
└── Exercises
```

- **Notes:** Explains the core concepts and syntax of the topic.
- **Examples:** Contains working examples of the learned syntax.
- **Exercises:** Used for problem-solving practice applying the topic.
