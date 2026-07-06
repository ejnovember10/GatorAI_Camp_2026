# Day 3: Dialogue Trees

On Day 2 you used **lists**. Today we go deeper on **dictionaries** - which store data as
`key: value` pairs - to build out our NPCs' dialogue!

## Step 1: Add a New Greeting
Open `dialogue_system.py` and find `@STUDENT-EDIT-Day3-1`.
The `fallbacks` variable is a **dictionary**: each character id (the key) maps to a line (the value). Change the greeting or add a new character. Notice `fallbacks.get(character_id, "default...")` - `.get()` returns the matching value, or a safe default if the key isn't found.

## Step 2: Branching Dialogue
Find `@STUDENT-EDIT-Day3-2`.
Create a branching dialogue option using nested lists or dictionaries so the NPC responds differently based on the player's choices.

## Step 3: Ending Conversations Early
Find `@STUDENT-EDIT-Day3-3`.
Add an option that ends the conversation early by setting `self.active = False` if the player chooses to walk away.
