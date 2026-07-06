# Day 1: Setup & Introduction

Welcome to PyDew Valley! Today we learn Python fundamentals - variables, printing,
errors, arithmetic, and data types - by exploring and editing our game. Work through
the steps **in order**; each one builds on the last.

> **How to find each spot:** open the file named in the step and use your editor's
> Find (Ctrl+F / Cmd+F) to search for the `@STUDENT-EDIT-...` marker.

## Step 1: Examine Datatypes and Add a Comment
Open `settings.py` and find `@STUDENT-EDIT-Day1-1`.
A **variable** is a name for a value. Identify the datatypes being used (strings, integers).
Write a **comment** using `#` to describe what a variable does - Python ignores everything after the `#`.
```python
# The width of the screen is 1280 pixels
SCREEN_WIDTH = 1280
```

## Step 2: Customize the Game Window Title
Open `settings.py` and find `@STUDENT-EDIT-Day1-2`.
Change the `TITLE` variable to a **string** of your choice (text in quotes). Make it your own game!
```python
TITLE = "My Awesome Farm Game"
```

## Step 3: Change the Window Size
Open `settings.py` and find `@STUDENT-EDIT-Day1-3`.
`SCREEN_WIDTH` and `SCREEN_HEIGHT` are **integers** (whole numbers). Change them and notice how the window changes when you run the game.

## Step 4: Experiment with Background Colors
Open `settings.py` and find `@STUDENT-EDIT-Day1-4`.
Change `WATER_COLOR` to a different hex code like `"#FF0000"` for red or `"#00FF00"` for green.

## Step 5: Print to the Console
Open `main.py` and find `@STUDENT-EDIT-Day1-5` inside the `__init__` method.
`print()` is a built-in **function** that displays text. Add:
```python
print("Game starting!")
```
Run the game (`python main.py`) and check your console output!

## Step 6: Combine Text and Variables with f-strings
Open `main.py` and find `@STUDENT-EDIT-Day1-6` (right below the last step).
Often you want to print text **and** a variable together. Use an **f-string** (note the `f` before the quotes, and the `{ }` around the variable):
```python
print(f"Welcome to {TITLE}!")
```
Run the game - the `{TITLE}` gets replaced with your game's title.

## Step 7: Read Your First Error Message
Errors are normal - everyone gets them! In `main.py`, temporarily add a line that uses a variable that doesn't exist:
```python
print(favorite_game)
```
Run the game. You'll see a `NameError`. **Read the LAST line of the error message** - it tells you the type of error and what went wrong (`name 'favorite_game' is not defined`). Now delete that line to fix it. Learning to read errors is a core skill!

> **Order matters:** Python runs your file top to bottom, so a variable must be **created before it is used**. That's exactly why `print(favorite_game)` failed - nothing had defined `favorite_game` yet.

## Step 7a: Create a Variable for Your Favorite Game!!!!!!!!
Create a variable named `favorite_game` and assign it the name of your favorite game as a string.

## Step 8: Use Variables in Calculations
Open `settings.py` and find `@STUDENT-EDIT-Day1-8`.
Variables can be used in **math**. `SCREEN_CENTER_X` and `SCREEN_CENTER_Y` are calculated from the screen size using `/` (division). Try adding a line to print one of them, then change the screen size and see the center change too.

## Step 9: Order of Operations (Playground)
Open `scratch.py` and find `@STUDENT-EDIT-Day1-9`. Run it with `python scratch.py`.
Python follows **PEMDAS** (Parentheses, Exponents, Multiply/Divide, Add/Subtract). Use `**` for powers - `^` does something totally different! Confirm the two exercises give `-5.0` and `9.75`, then try your own math.

## Step 10: Data Types and Type Casting
Open `scratch.py` and find `@STUDENT-EDIT-Day1-10` (and the matching note in `settings.py`).
Every value has a **type** (`int`, `float`, `str`, ...). Use `type()` to check it, and `int()` / `float()` to **convert** ("cast") between types. Notice that `int(3.99)` gives `3` - it *truncates*, it does **not** round!
