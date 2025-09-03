# Python Built-in Functions 🐍

Python comes with many **built-in functions** you can use without importing anything.  
These functions are helpful for working with numbers, strings, input/output, and more.

---

## 1. Input/Output

| Function | Description                          | Example |
|----------|--------------------------------------|---------|
| `print()` | Prints text or variables to the console | `print("Hello, world!")` |
| `input()` | Reads a line of text from the user    | `name = input("Enter your name: ")` |

---

## 2. Type Conversion

| Function | Description                 | Example |
|----------|-----------------------------|---------|
| `int()`  | Converts a value to an integer | `int("42") → 42` |
| `float()`| Converts a value to a float   | `float("3.14") → 3.14` |
| `str()`  | Converts a value to a string  | `str(123) → "123"` |

---

## 3. Basic Math Functions

| Function | Description                      | Example |
|----------|----------------------------------|---------|
| `abs()`  | Absolute value of a number       | `abs(-5) → 5` |
| `round()`| Rounds a number to nearest integer or given decimals | `round(3.14159, 2) → 3.14` |
| `max()`  | Returns the largest item         | `max(2, 5, 1) → 5` |
| `min()`  | Returns the smallest item        | `min(2, 5, 1) → 1` |
| `pow()`  | Raises a number to a power       | `pow(2, 3) → 8` |

---

## 4. Sequence Functions (not in slides)

| Function | Description                     | Example |
|----------|---------------------------------|---------|
| `len()`  | Returns the number of items in a sequence | `len("Python") → 6` |
| `range()`| Generates a sequence of numbers | `range(5)` → 0,1,2,3,4 |
| `sum()`  | Returns the sum of items in a sequence | `sum([1,2,3]) → 6` |

---

## 5. Other Useful Functions (not in slides)

| Function | Description                         | Example |
|----------|-------------------------------------|---------|
| `type()` | Returns the type of a value         | `type(42) → <class 'int'>` |
| `help()` | Displays help/documentation for objects | `help(print)` |
| `id()`   | Returns the unique ID of an object  | `id(42)` |

# Python Libraries and Non-Core Functions 📚🐍

Python comes with many **functions that are not in the core language**, but are available through libraries (also called modules).  
To use them, you must first **import the library**.

---

## Common Libraries

| Library   | Purpose / Example Functions           |
|-----------|--------------------------------------|
| `os`      | Interact with the operating system, e.g., change directory, list files |
| `math`    | Access special math functions such as `log()`, `sin()`, `sqrt()`, `pi` |
| `random`  | Random number generation, e.g., `random()`, `randint()` |
| `datetime`| Clock and calendar functions, e.g., `datetime.now()` |

## Python `math` Library Functions ➗📐

Python's `math` library provides advanced mathematical functions.  
You must `import math` to use them.

---

### 1. Rounding Functions

| Function      | Description |
|---------------|-------------|
| `math.floor(x)` | Returns the **largest integer** no bigger than `x` |
| `math.ceil(x)`  | Returns the **smallest integer** no less than `x` |

---

### 2. Exponential and Logarithmic Functions

| Function          | Description |
|------------------|-------------|
| `math.exp(x)`      | Exponential function \(e^x\) |
| `math.log(x)`      | Natural logarithm (log to the base `e` of `x`) |
| `math.log(x, b)`   | Logarithm of `x` to the base `b` |
| `math.sqrt(x)`     | Square root of `x` |

---

### 3. Trigonometric Functions

| Function           | Description |
|------------------|-------------|
| `math.sin(x)`       | Sine of `x` (in radians) |
| `math.asin(x)`      | Arcsine (inverse sine) of `x` (returns radians) |
| `math.degrees(x)`   | Converts angle `x` from **radians to degrees** |
| `math.radians(x)`   | Converts angle `x` from **degrees to radians** |

---

## Python `random` Library Functions 🎲

Python's `random` module provides functions for generating random numbers.  
You must `import random` to use these functions.

---

### 1. `randint(a, b)`
Returns a **random integer** between `a` and `b`, **inclusive**.

### 2. `randrange(a, b)`

Returns a random integer between a and b-1 (upper bound is exclusive).

### 3. `random()`

Returns a random float in the range [0.0, 1.0) (0 inclusive, 1 exclusive).

---

# Python `import` Statements 📦

There are several ways to import modules and functions in Python. Each affects how you access names in the module.


## 1. Import the Module

```python
import random      # imports the module itself
random()           # ❌ Error: module is not callable
random.random()    # ✅ Call a function from the module
```
- When you call a function, you must prefix with module name

## 2. Import Specific Names

```python
from random import random   # import only the 'random' function
random()                     # ✅ Works
randint(0, 9)                # ❌ Error: 'randint' not imported
```
- Only the names explicitly imported are directly available

## 3. Import All Names

```python
from random import *    # import all names from the module
random()                 # ✅ Works
randint(0, 9)            # ✅ Works
```
- All public names from the module can be used directly without prefix
- Could lead to name conflicts

# Python Character Operations & Escape Sequences 🅰️🔣

Python provides functions and tools for working with characters and special characters in strings.

---

## 1. Character Functions

| Function | Description | Example | Result |
|----------|------------|---------|--------|
| `ord(c)` | Returns the ASCII code of character `c` | `ord('A')` | `65` |
| `chr(n)` | Returns the character corresponding to ASCII code `n` | `chr(65)` | `'A'` |

---

## 2. Escape Sequences

Some characters (like quotes, tabs, or newlines) cannot be used directly in strings.  
Escape sequences allow you to include them safely.

| Escape Sequence | Name / Purpose |
|-----------------|----------------|
| `\b`             | Backspace |
| `\t`             | Tab |
| `\n`             | Newline |
| `\f`             | Formfeed |
| `\\`             | Backslash `\` |
| `\'`             | Single quote `'` |
| `\"`             | Double quote `"` |
| `\r`             | Carriage return |

**Example:**

```python
print("He said: \"Hello\"")  # Output: He said: "Hello"
print("Column1\tColumn2")    # Output: Column1    Column2
print("Line1\nLine2")        # Output: Line1
                             #         Line2
```

## 3. Printing Without a Newline
By default, `print()` adds a newline at the end.
You can override this with the `end` parameter:
```python
print("Hello", end=" ")  # stays on the same line
print("World")           # Output: Hello World
```

## 4. Printing with Custom Separation
The `sep` parameter defines the separator between multiple arguments in print():
```python
print("A", "B", "C", sep="-")  # Output: A-B-C
print(1, 2, 3, sep=", ")       # Output: 1, 2, 3
```

# Python String Operations & Formatting 📝

This file covers string concatenation, formatting, and related operations in Python.

---

## 1. String Concatenation

### a) Using the `+` Operator
Combine two strings explicitly:

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"
```

### b) String Literal Concatenation
- Python allows placing two string literals next to each other without an operator.
- **Only works with literals, not variables:**
- Use `+` with variables or lists to avoid mistakes.

```python
newStr = "abc" "def" "ghi"
print(newStr)  # Output: abcdefghi

str1 = "abc"
# str1 "def"  # ❌ SyntaxError: cannot concatenate variables without '+'
```

## 2. Formatting with `format()`
`format(value, format_string)` converts a value to a string with specific formatting

### a) Formatting Floats
- Field width: total width of the string
- Precision: number of digits after the decimal
- If the field is too narrow, Python expands it automatically. 
- You can also format floats in scientific notation, percentages, or left-justify with `<`.

```python
format(123.456789, "10.2f")       # '    123.46' (right justified)
format(123456.7891234, "8.3f")    # '123456.789'
format(123, "8.3f")               # '  123.000'
```

### b) Formatting Integers
- Decimal, hexadecimal, octal, or binary
- Can specify field width

```python
format(255, "8d")      # Decimal, right justified: '     255'
format(255, "8x")      # Hexadecimal: '      ff'
format(255, "8b")      # Binary: '11111111'
```

### c) Formatting Strings
- Strings are left justified by default 
- Use `>` to right justify, `<` to left justify, or `^` to center

```python
format("Hello", "10")   # Left justified: 'Hello     '
format("Hello", ">10")  # Right justified: '     Hello'
format("Hello", "^10")  # Centered: '  Hello   '
```

## 3. Printing Multiple Values
- `print()` automatically converts each argument to a string and separates by space
- Use `sep` to change separator: `print(1, 2, 3, sep="-")` → `1-2-3` 
- Use `end` to avoid newline: `print("Hello", end=" ")`