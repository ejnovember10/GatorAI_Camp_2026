# Day 5: Polish & Personalization

Let's polish our game, add personal touches, and take a first peek at the AI you'll build
in Week 2!

## Step 1: Customize Player Identity
Open `settings.py` and find `@STUDENT-EDIT-Day5-1`.
Customize the `PLAYER_NAME` and `GREETING` variables to give your player a unique identity. Tip: weave `PLAYER_NAME` into dialogue with an f-string, e.g. `f"Welcome back, {PLAYER_NAME}!"`.

## Step 2: Custom Animations
Open `player.py` and find `@STUDENT-EDIT-Day5-2`.
Add a custom animation folder path here (like `'celebrate'`) so your character can do a little dance!

## Step 3: Loading Text Files
Open `dialogue_system.py` and find `@STUDENT-EDIT-Day5-3`.
Instead of hardcoding all the text, try loading your custom dialogue from a `.txt` file using Python's `open()` function.

## Step 4: From Your Python to Real AI (Bridge to Week 2)
Open `bridge_to_week2.py` and find `@STUDENT-EDIT-Day5-4`. Run it with `python bridge_to_week2.py`.
This tiny program uses **only what you learned this week** (variables, a list, a dictionary, a function, `.get()`, and f-strings) to turn an emotion into an NPC reply:

`INPUT (emotion) -> lookup -> OUTPUT (reply)`

Next week, the game will detect your **real** emotion from the webcam and use an AI model instead of this hand-written dictionary - but it's the exact same shape! Add your own emotions and lines to `EMOTION_REPLIES`, then run it again.
