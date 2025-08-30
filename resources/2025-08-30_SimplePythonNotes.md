# Variables and Assignments

Variables are not declared like other programming languages

If you 'define' a variable multiple times, it becomes reassigned

### Naming Conventions and Rules
- Name begins with letter or underscore
- After first letter, any combination of letters, underscores, or digits may be used
- You cannot use Python's reserved words:
  - and, as, assert, break, class, continue,
def, del, elif, else, except, False, finally, for, from, global, if, import, in,
is, lambda, nonlocal, None, not, or,
pass, raise, return, True, try, while,
with, yield
- Variable names should begin with **lowercase** letter
- Choose meaningful names
- Loop variables can be single letters
- Good practice is using **camelCase**

### Python Data Types
- Strings: immutable
  - `'Wikipedia'`
- Numbers: immutable
  - int: fixed precision
    - `42`
  - float: floating point number with precision defined by system
    - `3.1415927`
    - `3.5e7`
- Lists: mutable and can have mixed types
  - `[4.0, 'string', True, 4.0]`
- Tuples: immutable, can have mixed types
  - `(4.0, 'string', True)`
- Dictionary: mutable group of key and value pairs
  - `{key1: 1.0, 3: False}`
- Sets: mutable, unordered, no duplicates
  - `{4.0, 'string', True}`
- Boolean: immutable truth value
  - `True, False`
- Bytes: immutable sequence of bytes
  - `b'Some ASCII'`

# Arithmetic Operations
| Operator | Meaning        | Example  | Result     |
| -------- | -------------- | -------- | ---------- |
| `+`      | Addition       | `7 + 3`  | `10`       |
| `-`      | Subtraction    | `7 - 3`  | `4`        |
| `*`      | Multiplication | `7 * 3`  | `21`       |
| `/`      | Division       | `7 / 3`  | `2.333...` |
| `//`     | Floor Division | `7 // 3` | `2`        |
| `%`      | Modulus        | `7 % 3`  | `1`        |
| `**`     | Exponentiation | `2 ** 4` | `16`       |


# Augmented Assignment Operators in Python 🎯

Augmented assignments update a variable "in place" by applying an operation and reassigning the result.

---

## Table of Operators

| Operator | Meaning                       | Example Before | Statement     | Example After |
|----------|-------------------------------|----------------|---------------|---------------|
| `+=`     | Add and assign                | `x = 5`        | `x += 3`      | `x == 8`      |
| `-=`     | Subtract and assign           | `x = 5`        | `x -= 2`      | `x == 3`      |
| `*=`     | Multiply and assign           | `x = 4`        | `x *= 3`      | `x == 12`     |
| `/=`     | Divide and assign (float)     | `x = 9`        | `x /= 2`      | `x == 4.5`    |
| `//=`    | Floor divide and assign       | `x = 9`        | `x //= 2`     | `x == 4`      |
| `%=`     | Modulus and assign            | `x = 9`        | `x %= 2`      | `x == 1`      |
| `**=`    | Exponentiate and assign       | `x = 3`        | `x **= 2`     | `x == 9`      |

# Simultaneous and Multiple Assignment in Python 🧩

Python lets you assign values to multiple variables at once.  
This is useful for cleaner code, swapping values, and unpacking sequences.

---

## Table of Assignments

| Syntax                  | Name/Meaning               | Example Code           | Result                      |
|--------------------------|----------------------------|------------------------|-----------------------------|
| `a, b = 1, 2`           | **Simultaneous Assignment** | `a, b = 1, 2`          | `a == 1`, `b == 2`          |
| `x = y = z = 0`         | **Multiple Assignment**     | `x = y = z = 0`        | All three are `0`           |
| `a, b = b, a`           | **Swap Variables**          | `a, b = 5, 10` → `a, b = b, a` | `a == 10`, `b == 5` |
| `p, q, r = [1, 2, 3]`   | **Unpacking a Sequence**    | `p, q, r = [1, 2, 3]`  | `p == 1`, `q == 2`, `r == 3` |
| `x, y, *rest = [1,2,3,4]` | **Extended Unpacking**    | `x, y, *rest = [1,2,3,4]` | `x == 1`, `y == 2`, `rest == [3,4]` |