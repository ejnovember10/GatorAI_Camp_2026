# Day 2: Sprites & Game Logic

Today we learn about lists, naming, libraries, and functions - then use them to modify
the player and add a character! Work through the steps **in order**.

## Step 1: Lists and Zero-Indexing
Open `player.py` and search for `self.tools`. You'll see a **list** (values in square brackets):
```python
self.tools = ["hoe", "axe", "water"]
```
Lists hold an ordered sequence of items and can even mix types (e.g. `[1, 35, 5.6, "Fun"]`).
Python is **zero-indexed**: `self.tools[0]` is `"hoe"`, `self.tools[1]` is `"axe"`. The player's animation frames are stored in lists too!

## Step 2: Good Variable Naming
Open `settings.py` and find `@STUDENT-EDIT-Day2-6`.
Names should be **meaningful** and follow the rules: letters/digits/underscores only, no leading digit, no `$` or spaces. Python is **case-sensitive** (`Robin` ≠ `robin`). PEP8 style prefers `lower_case_with_underscores`.

## Step 3: Add a Custom Character
Open `settings.py` and find `@STUDENT-EDIT-Day2-1`.
Add a custom sprite image name to the character dictionary. Give your new NPC a good, meaningful **name** (that's the dictionary key) - you just used Step 2!

## Step 4: Comments - Explain the "Why"
You met `#` comments on Day 1. Now practice writing them well: comment *why* something happens, not the obvious. Add a helpful comment above one of your edits so your future self understands it.

## Step 5: Libraries and Import Styles
Open `main.py` and find `@STUDENT-EDIT-Day2-8` (near the top imports).
A **library** is pre-written code you `import`. Notice the three import styles in the comment. In a terminal, try `help(pygame)` or `dir(pygame)` to explore what a library offers.

## Step 6: Read and Write a Function
Open `support.py` and find `@STUDENT-EDIT-Day2-7`.
You'll see two real **functions** above it. Now write your own! A function has a `def` line, a docstring, indented code, and a `return`:
```python
def add(x, y):
    '''Take two values and return their sum.'''
    return x + y
```
Then call it: `add(3, 4)` gives `7`. Challenge: write a `square(n)` function that returns `n ** 2`.

## Step 7: Change Player Speed
Open `settings.py` and find `@STUDENT-EDIT-Day2-2`.
Change the `PLAYER_SPEED` variable to make the player move faster or slower.

## Step 8: Modify Starting Direction
Open `player.py` and find `@STUDENT-EDIT-Day2-3`.
Change the player's starting direction from `"down_idle"` to `"left_idle"`, `"right_idle"`, or `"up_idle"`.

## Step 9: Add a Boundary Check (Conditionals)
Open `player.py` and find `@STUDENT-EDIT-Day2-4`.
Add an `if` statement to prevent the player from leaving the screen vertically:
```python
if self.pos.y < 0:
    self.pos.y = 0
```

## Step 10: WASD Movement Control (Logical `or`)
Open `player.py` and find `@STUDENT-EDIT-Day2-5`.
Let the player move with WASD **or** the arrow keys using the logical `or` operator:
```python
if keys[pygame.K_UP] or keys[pygame.K_w]:
    self.direction.y = -1
    self.status = "up"
```
Do this for all four directions!

## Step 11: Tuples, Arguments, and None (Playground)
Open `scratch.py` and find `@STUDENT-EDIT-Day2-9`. Run it with `python scratch.py`.
- A function can **return more than one value** - Python packs them into a **tuple** you can **unpack** into separate variables.
- **Argument order matters** (positional arguments): `describe(3, 4)` differs from `describe(4, 3)`.
- A function with no `return` gives back the special value `None`.
- **Default arguments**: an input can have a default value - `add(2)` uses it, `add(2, 6)` overrides it.

You can also see real tuples in `settings.py` at `@STUDENT-EDIT-Day2-9` (the `(x, y)` coordinate pairs).
