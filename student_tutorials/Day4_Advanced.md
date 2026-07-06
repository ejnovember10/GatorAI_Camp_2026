# Day 4: Advanced Dialogue and Debugging

Today we add advanced dialogue features and go **deeper on debugging** - building on the
error-reading you started on Day 1.

## Step 1: Debugging Dialogue Branches
Open `dialogue_system.py` and find `@STUDENT-EDIT-Day4-1`.
When branching dialogue gets complex, it's hard to tell which branch is running. Add a `print("Executing branch A")` statement to help you debug!

## Step 2: Linking Dialogue to Sprite Actions
Find `@STUDENT-EDIT-Day4-2` in `dialogue_system.py`.
When a dialogue option is selected, you can trigger a change in the game state! For example, try changing an NPC's direction if they get angry.

## Step 3: Read a Traceback (Deliberately Break It)
Errors help you learn. On purpose, remove a colon `:` or mis-indent a line inside a function, then run the game. Read the **traceback from the bottom up**: the last line names the error type (`IndentationError`, `KeyError`, `IndexError`, `NameError`) and the file/line. Fix it, and you've leveled up your debugging.

## Step 4: Variable Scope
A variable created **inside** a function only exists inside that function (it is *local*). If you need its value outside, you must `return` it. Try printing a variable that was only set inside a function - you'll get a `NameError`, which proves the point!
