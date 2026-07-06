"""
scratch.py - Your Python Playground
===================================
This file is a SCRATCH PAD. It is not part of the game - it's a safe place to practice
some pure-Python ideas that don't have a natural home in the game.

Run it any time with:   python scratch.py

Read each section, predict the output, then run it to check yourself. You can change
anything here - you cannot break the game from this file.
"""

# =============================================================================
# @STUDENT-EDIT-Day1-9: ORDER OF OPERATIONS (PEMDAS)
# =============================================================================
# Python does math in the usual order: Parentheses, Exponents (**), Multiply/Divide,
# then Add/Subtract. IMPORTANT: use ** for "to the power of". The ^ symbol is NOT a
# power in Python (it is a bitwise XOR) - a classic beginner trap!

# Exercise 2 from the notebook: compute (100 - 5^3) / 5   (answer should be -5.0)
answer_2 = (100 - 5**3) / 5
print(f"Exercise 2: (100 - 5**3) / 5 = {answer_2}")  # expect -5.0

# Exercise 3 from the notebook: divide 15 by 4 and add 6  (answer should be 9.75)
answer_3 = 15 / 4 + 6
print(f"Exercise 3: 15 / 4 + 6 = {answer_3}")  # expect 9.75


# =============================================================================
# @STUDENT-EDIT-Day1-10: DATA TYPES AND TYPE CASTING
# =============================================================================
# Every value has a type. Use type() to check it, and int()/float()/str() to convert
# ("cast") between types.

x = 3.14
print(f"The type of x (3.14) is: {type(x)}")  # <class 'float'>

# Cast float -> int. NOTE: this TRUNCATES toward zero, it does NOT round!
y = int(x)
print(f"int(3.14) = {y}  (type is now {type(y)})")  # 3, not 4

# Proof it truncates and doesn't round: even 3.99 becomes 3
print(f"int(3.99) = {int(3.99)}  (truncates - does NOT round up to 4)")

# Cast int -> float (notice the .0 that gets added)
z = float(y)
print(f"float(3) = {z}  (type is now {type(z)})")  # 3.0


# =============================================================================
# @STUDENT-EDIT-Day2-9: FUNCTIONS THAT RETURN MANY VALUES (TUPLES) + ARGUMENTS
# =============================================================================
def powers(number):
    """Take a number and return its square, cube, and 4th power."""
    return number**2, number**3, number**4


# If you catch the result in ONE variable, Python packs them into a TUPLE:
values = powers(2)
print(f"powers(2) returned a tuple: {values}")  # (4, 8, 16)
print(f"The cube (index 1) is: {values[1]}")

# Or "unpack" the tuple into THREE names at once:
square, cube, fourth = powers(3)
print(f"3 squared={square}, cubed={cube}, 4th power={fourth}")
# TRY THIS: change the line above to use 2 or 4 names - you'll get a mismatch error!


# POSITIONAL ARGUMENTS: the ORDER you pass arguments in matters.
def describe(first, second):
    """Print the two arguments in the order they were received."""
    print(f"first={first}, second={second}")


describe(3, 4)  # first=3, second=4
describe(4, 3)  # first=4, second=3  <- different result, because position matters!


# A function with NO `return` statement gives back the special value None:
def just_prints(a):
    print(f"(just_prints is showing: {a})")


result = just_prints(5)
print(f"just_prints returned: {result}")  # None


# DEFAULT VALUES: an argument can have a default that's used when you don't pass one.
def add(x, y=1):
    """Add two numbers; y defaults to 1 when it isn't given."""
    return x + y


print(f"add(2) uses the default y=1     -> {add(2)}")  # 3
print(f"add(2, 6) overrides the default -> {add(2, 6)}")  # 8
