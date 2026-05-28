# Day 3: Dialogue Trees and Interactions

## Objective
Create branching conversations and interactive dialogue systems.

## Core Concepts
- **Introduction to Dialogue Trees**
  - Branching conversation options
  - Store dialogue in data structures (lists/dictionaries)
- **Using Lists or Dictionaries (Basic)**
  
  Example dictionary approach:
  ```python
  dialogue = { 
    "greeting": "Hello, traveler!", 
    "option1": "Where am I?",
    "option2": "Who are you?" 
  }
  ```
- **Loops for Navigating Dialogue**
  - `for` loops to cycle through dialogue options
  - Conditionals for conversation branching

## Exercise: Implementing a Basic Conversation
- Give newly added sprite a short conversation
- Use `input()` for dialogue selection and response branching
- **Deliverable**: Push project to personal GitHub repository

## Code References

### Dialogue System Overview
**File**: `dialogue_system.py` (Lines 1-100)
- Shows the main dialogue system class
- Demonstrates how dialogue is stored and displayed
- Illustrates AI integration for dynamic content

```python
"""
PyDew Valley - Dialogue System
=============================
This module manages character dialogue in the game, providing a flexible
framework for conversations with NPCs (Non-Player Characters).

Educational Concepts Covered:
- Data structures (dictionaries, lists)
- Text rendering and display
- User interface design
- State management
- Event handling and input processing
- Modular code organization

This system can be easily extended to support:
- Multiple characters with unique dialogue
- Branching conversations
- Character mood/emotion responses
- Quest-related dialogue
- Dynamic dialogue based on game state
"""

import pygame
from settings import *
from timer import Timer
import game_settings

# Try to import AI dialogue manager, fall back gracefully if it fails
try:
    from ai_dialogue_manager import AIDialogueManager

    AI_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ AI Dialogue Manager not available: {e}")
    AI_AVAILABLE = False


class DialogueSystem:
    """
    Manages displaying NPC dialogue in a text box on screen, with support for
    AI-generated dynamic content.
    """

    def __init__(self):
        """Initialize the dialogue system and its components."""
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)
        self.active = False
        self.current_dialogue = []
        self.dialogue_index = 0
        self.dialogue_timer = Timer(200)
        self.skip_next = False
        self.ai_manager = AIDialogueManager() if AI_AVAILABLE else None
```

**DETAILED WALKTHROUGH:**
Let's examine our dialogue system in detail:

1. **Module Docstring (Lines 1-15)**:
   ```python
   """
   PyDew Valley - Dialogue System
   =============================
   This module manages character dialogue in the game, providing a flexible
   framework for conversations with NPCs (Non-Player Characters).

   Educational Concepts Covered:
   - Data structures (dictionaries, lists)
   - Text rendering and display
   - User interface design
   - State management
   - Event handling and input processing
   - Modular code organization

   This system can be easily extended to support:
   - Multiple characters with unique dialogue
   - Branching conversations
   - Character mood/emotion responses
   - Quest-related dialogue
   - Dynamic dialogue based on game state
   """
   ```
   - This docstring does double duty: it explains what the file does AND lists the educational concepts covered
   - It also mentions potential extensions, giving students ideas for how they could expand the system

2. **Imports (Lines 18-21)**:
   ```python
   import pygame
   from settings import *
   from timer import Timer
   import game_settings
   ```
   - `pygame`: For rendering text and handling input
   - `from settings import *`: Game configuration (screen size, fonts, etc.)
   - `from timer import Timer`: A custom timer class we've created for controlling dialogue pacing
   - `import game_settings`: Audio and other game-specific settings

3. **Optional AI Import (Lines 24-30)**:
   ```python
   # Try to import AI dialogue manager, fall back gracefully if it fails
   try:
       from ai_dialogue_manager import AIDialogueManager

       AI_AVAILABLE = True
   except ImportError as e:
       print(f"⚠️ AI Dialogue Manager not available: {e}")
       AI_AVAILABLE = False
   ```
   - This is a great example of defensive programming!
   - We try to import the AI dialogue manager, but if it's not available (maybe the openai library isn't installed), we don't crash
   - Instead, we set a flag (`AI_AVAILABLE = False`) and print a helpful message
   - This allows the game to run in "offline mode" with predefined dialogue when AI isn't available

4. **Class Definition (Line 33)**:
   ```python
   class DialogueSystem:
   ```
   - Defines our main dialogue system class

5. **Class Docstring (Lines 34-38)**:
   ```python
   """
   Manages displaying NPC dialogue in a text box on screen, with support for
   AI-generated dynamic content.
   """
   ```
   - A concise explanation of what this class does

6. **Constructor Method (Line 41)**:
   ```python
   def __init__(self):
   ```
   - The constructor that sets up our dialogue system when we create an instance

7. **Initialization (Lines 44-51)**:
   ```python
   """Initialize the dialogue system and its components."""
   self.display_surface = pygame.display.get_surface()
   self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)
   self.active = False
   self.current_dialogue = []
   self.dialogue_index = 0
   self.dialogue_timer = Timer(200)
   self.skip_next = False
   self.ai_manager = AIDialogueManager() if AI_AVAILABLE else None
   ```
   - Let's break down each line:
   - `self.display_surface = pygame.display.get_surface()`: Gets the main screen surface to draw on
   - `self.font = pygame.font.Font("font/LycheeSoda.ttf", 30)`: Loads a custom font at size 30 for rendering text
   - `self.active = False`: Boolean flag to track if dialogue is currently being shown
   - `self.current_dialogue = []`: List to hold the dialogue lines we're currently displaying
   - `self.dialogue_index = 0`: Index to track which line of dialogue we're on
   - `self.dialogue_timer = Timer(200)`: Timer to prevent dialogue from advancing too quickly (200ms = 0.2 seconds)
   - `self.skip_next = False`: Flag to handle input debouncing (prevents multiple advances from one key press)
   - `self.ai_manager = AIDialogueManager() if AI_AVAILABLE else None`: Creates an AI manager if available, otherwise sets to None

### Dialogue Data Structures
**File**: `dialogue_system.py` (Lines 100-200)
- Shows how dialogue is stored in lists and dictionaries
- Demonstrates methods for setting and advancing dialogue

```python
    def set_dialogue(self, dialogue_list):
        """Set the dialogue to be displayed."""
        self.current_dialogue = dialogue_list
        self.dialogue_index = 0
        self.active = True
        self.dialogue_timer.activate()
```

**DETAILED WALKTHROUGH:**
This method sets up a new dialogue to be displayed:

1. **Method Definition (Line 102)**:
   ```python
   def set_dialogue(self, dialogue_list):
   ```
   - Takes a parameter `dialogue_list` which should be a list of strings

2. **Method Docstring (Lines 103-104)**:
   ```python
   """Set the dialogue to be displayed."""
   ```
   - Simple explanation of what the method does

3. **Implementation (Lines 105-108)**:
   ```python
   self.current_dialogue = dialogue_list
   self.dialogue_index = 0
   self.active = True
   self.dialogue_timer.activate()
   ```
   - `self.current_dialogue = dialogue_list`: Stores the dialogue lines we want to show
   - `self.dialogue_index = 0`: Resets to the first line (index 0)
   - `self.active = True`: Marks that dialogue is now active and should be displayed
   - `self.dialogue_timer.activate()`: Starts our timer so we can control how fast dialogue advances

### Input Handling for Dialogue Progression
**File**: `dialogue_system.py` (Lines 109-130)
- Shows how we handle keyboard input to advance dialogue
- Demonstrates input debouncing techniques

```python
    def input(self):
        """Handle keyboard input for dialogue progression."""
        keys = pygame.key.get_just_pressed()
        
        if keys[pygame.K_SPACE] and not self.skip_next:
            self.dialogue_index += 1
            if self.dialogue_index >= len(self.current_dialogue):
                self.active = False
                self.dialogue_index = 0
            else:
                self.dialogue_timer.activate()
        
        if keys[pygame.K_SPACE]:
            self.skip_next = True
        else:
            self.skip_next = False
```

**DETAILED WALKTHROUGH:**
This is where we handle player input to advance through dialogue:

1. **Method Definition (Line 111)**:
   ```python
   def input(self):
   ```
   - Method that handles input for the dialogue system

2. **Method Docstring (Lines 112-113)**:
   ```python
   """Handle keyboard input for dialogue progression."""
   ```
   - Explains what this method does

3. **Getting Key States (Line 115)**:
   ```python
   keys = pygame.key.get_just_pressed()
   ```
   - `pygame.key.get_just_pressed()` returns a boolean array showing which keys were just pressed since the last frame
   - This is different from `get_pressed()` which shows which keys are currently held down
   - Using `get_just_pressed()` helps prevent multiple triggers from a single key press

4. **Spacebar Check with Debouncing (Lines 117-124)**:
   ```python
   if keys[pygame.K_SPACE] and not self.skip_next:
       self.dialogue_index += 1
       if self.dialogue_index >= len(self.current_dialogue):
           self.active = False
           self.dialogue_index = 0
       else:
           self.dialogue_timer.activate()
   
   if keys[pygame.K_SPACE]:
       self.skip_next = True
   else:
       self.skip_next = False
   ```
   - Let's break this down:
   - `if keys[pygame.K_SPACE] and not self.skip_next:`: Checks if spacebar was just pressed AND we're not in a skip state
   - `self.dialogue_index += 1`: Advances to the next dialogue line
   - `if self.dialogue_index >= len(self.current_dialogue):`: Checks if we've gone past the last line
   - `self.active = False`: If so, deactivates the dialogue system
   - `self.dialogue_index = 0`: Resets the index for next time
   - `else:`: If we haven't reached the end...
   - `self.dialogue_timer.activate()`: ...restart the timer to prevent immediate further advancement
   - The bottom part handles the skip flag:
   - `if keys[pygame.K_SPACE]: self.skip_next = True`: If spacebar is pressed, set skip flag
   - `else: self.skip_next = False`: If spacebar is not pressed, clear skip flag
   - This debouncing technique ensures that holding down the spacebar doesn't blast through dialogue too quickly

### Drawing Dialogue to Screen
**File**: `dialogue_system.py` (Lines 131-160)
- Shows how we actually render the dialogue text on screen
- Demonstrates text wrapping and positioning

```python
    def draw(self):
        """Draw the dialogue box and text on screen."""
        if not self.active:
            return
        
        # Dialogue box dimensions and position
        box_width = self.display_surface.get_width() - 200
        box_height = 200
        box_x = 100
        box_y = self.display_surface.get_height() - box_height - 100
        
        # Draw dialogue box background
        pygame.draw.rect(self.display_surface, '#222222', (box_x, box_y, box_width, box_height))
        pygame.draw.rect(self.display_surface, '#111111', (box_x, box_y, box_width, box_height), 4)
        
        # Draw dialogue text
        if self.dialogue_index < len(self.current_dialogue):
            text = self.current_dialogue[self.dialogue_index]
            lines = self._wrap_text(text, box_width - 40)
            for i, line in enumerate(lines):
                text_surface = self.font.render(line, False, '#EEEEEE')
                text_rect = text_surface.get_rect(topleft = (box_x + 20, box_y + 20 + i * 30))
                self.display_surface.blit(text_surface, text_rect)
```

**DETAILED WALKTHROUGH:**
This is where we actually draw the dialogue to the screen:

1. **Method Definition (Line 133)**:
   ```python
   def draw(self):
   ```
   - Method responsible for rendering the dialogue

2. **Method Docstring (Lines 134-135)**:
   ```python
   """Draw the dialogue box and text on screen."""
   ```
   - Simple explanation

3. **Early Exit Check (Lines 137-138)**:
   ```python
   if not self.active:
       return
   ```
   - If dialogue isn't active, we don't need to draw anything - exit early for efficiency

4. **Box Dimensions and Position (Lines 141-145)**:
   ```python
   # Dialogue box dimensions and position
   box_width = self.display_surface.get_width() - 200
   box_height = 200
   box_x = 100
   box_y = self.display_surface.get_height() - box_height - 100
   ```
   - We calculate the size and position of our dialogue box
   - Width: screen width minus 200 pixels (100px margin on each side)
   - Height: fixed at 200 pixels
   - X: 100 pixels from left edge
   - Y: positioned near the bottom of the screen

5. **Drawing the Box Background (Lines 148-149)**:
   ```python
   # Draw dialogue box background
   pygame.draw.rect(self.display_surface, '#222222', (box_x, box_y, box_width, box_height))
   pygame.draw.rect(self.display_surface, '#111111', (box_x, box_y, box_width, box_height), 4)
   ```
   - First draws a dark gray rectangle (#222222) for the box fill
   - Then draws a slightly darker rectangle (#111111) with a thickness of 4 pixels for the border
   - This creates a nice bordered box effect

6. **Drawing the Text (Lines 152-160)**:
   ```python
   # Draw dialogue text
   if self.dialogue_index < len(self.current_dialogue):
       text = self.current_dialogue[self.dialogue_index]
       lines = self._wrap_text(text, box_width - 40)
       for i, line in enumerate(lines):
           text_surface = self.font.render(line, False, '#EEEEEE')
           text_rect = text_surface.get_rect(topleft = (box_x + 20, box_y + 20 + i * 30))
           self.display_surface.blit(text_surface, text_rect)
   ```
   - First checks if we have a valid dialogue index
   - Gets the current line of text to display
   - Calls a helper method `_wrap_text` to break long lines into multiple lines that fit in our box
   - Loops through each line of wrapped text:
     - Renders the text surface with our font and light gray color (#EEEEEE)
     - Gets the rectangle for positioning the text
     - Draws (blits) the text onto the display surface with 20px padding inside the box
     - Each subsequent line is positioned 30 pixels lower (line spacing)

### AI Dialogue Manager Integration
**File**: `ai_dialogue_manager.py` (Lines 1-100)
- Shows how AI integration works for dynamic dialogue
- Demonstrates API key handling and fallback mechanisms

```python
try:
    import openai
except ImportError:
    print("⚠️ OpenAI library not installed. AI dialogue will use fallback mode.")
    openai = None

import os
import json
from typing import Dict, List, Optional


class AIDialogueManager:
    """
    Manages all AI-powered dialogue features, including API connection,
    content generation, and fallback mechanisms.
    """

    def __init__(self, key_file_path: str = "ai_materials/navigator_api_key.json"):
        """Initialize the AI manager and set up the API client."""
        self.client = None
        self.fallback_mode = True

        # Check if OpenAI is available
        if openai is None:
            print("🔄 AI Manager initialized in offline mode (OpenAI not available).")
            return

        self.credentials = self._load_api_credentials(key_file_path)

        if self.credentials:
            try:
                self.client = openai.OpenAI(
                    api_key=self.credentials["api_key"],
                    base_url=self.credentials["base_url"],
                )
                self.fallback_mode = False
                print("🤖 AI Dialogue Manager initialized with API access.")
            except Exception as e:
                print(
                    f"⚠️ AI Manager could not connect, falling back to offline mode: {e}"
                )
                self.fallback_mode = True
        else:
            print("🔄 AI Manager initialized in offline (fallback) mode.")

    def _load_api_credentials(self, key_file_path: str) -> Optional[Dict[str, str]]:
        """Load API credentials from a JSON file."""
        try:
            with open(key_file_path, "r") as file:
                data = json.load(file)
                return {
                    "api_key": data.get("api_key"),
                    "base_url": data.get("base_url"),
                }
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"⚠️ Could not load API credentials: {e}")
                return None
```

**DETAILED WALKTHROUGH:**
This is our AI-powered dialogue manager that can generate dynamic content:

1. **Optional OpenAI Import (Lines 1-4)**:
   ```python
   try:
       import openai
   except ImportError:
       print("⚠️ OpenAI library not installed. AI dialogue will use fallback mode.")
       openai = None
   ```
   - Another example of defensive programming!
   - We try to import the openai library, but if it's not installed, we set `openai = None` and print a helpful message
   - This allows our code to continue working even if the AI dependencies aren't available

2. **Standard Imports (Lines 6-8)**:
   ```python
   import os
   import json
   from typing import Dict, List, Optional
   ```
   - `os`: For interacting with the operating system (file paths, etc.)
   - `json`: For reading and writing JSON files (we'll use this for API credentials)
   - `from typing import Dict, List, Optional`: Type hints for better code documentation and IDE support

3. **Class Definition (Line 11)**:
   ```python
   class AIDialogueManager:
   ```
   - Defines our AI dialogue manager class

4. **Class Docstring (Lines 12-16)**:
   ```python
   """
   Manages all AI-powered dialogue features, including API connection,
   content generation, and fallback mechanisms.
   """
   ```
   - Explains what this class does

5. **Constructor Method (Line 18)**:
   ```python
   def __init__(self, key_file_path: str = "ai_materials/navigator_api_key.json"):
   ```
   - Constructor that takes an optional path to an API key file
   - Defaults to "ai_materials/navigator_api_key.json" if no path is provided
   - Shows type hinting for the parameter (`str`)

6. **Initialization (Lines 21-22)**:
   ```python
   """Initialize the AI manager and set up the API client."""
   self.client = None
   self.fallback_mode = True
   ```
   - Docstring explaining what the constructor does
   - Initialize `self.client` to None (will hold our OpenAI client if available)
   - Start with `fallback_mode = True` (assume we'll need to use fallback dialogue)

7. **OpenAI Availability Check (Lines 25-28)**:
   ```python
   # Check if OpenAI is available
   if openai is None:
       print("🔄 AI Manager initialized in offline mode (OpenAI not available).")
       return
   ```
   - If we couldn't import openai earlier, we print a message and exit the constructor early
   - The emojis (🔄) are just for visual feedback in the console

8. **Loading API Credentials (Lines 31-32)**:
   ```python
   self.credentials = self._load_api_credentials(key_file_path)
   ```
   - Calls a helper method to load API credentials from a JSON file

9. **Setting Up API Client (Lines 34-44)**:
   ```python
   if self.credentials:
       try:
           self.client = openai.OpenAI(
               api_key=self.credentials["api_key"],
               base_url=self.credentials["base_url"],
           )
           self.fallback_mode = False
           print("🤖 AI Dialogue Manager initialized with API access.")
       except Exception as e:
           print(
               f"⚠️ AI Manager could not connect, falling back to offline mode: {e}"
           )
           self.fallback_mode = True
   ```
   - If we successfully loaded credentials...
   - Try to create an OpenAI client with the API key and base URL
   - If successful, set `fallback_mode = False` and print success message
   - If any exception occurs, fall back to offline mode and print error details

10. **Handling Missing Credentials (Lines 46-47)**:
    ```python
    else:
        print("🔄 AI Manager initialized in offline (fallback) mode.")
    ```
    - If we didn't get valid credentials, initialize in offline mode

11. **Credential Loading Helper (Lines 50-63)**:
    ```python
    def _load_api_credentials(self, key_file_path: str) -> Optional[Dict[str, str]]:
        """Load API credentials from a JSON file."""
        try:
            with open(key_file_path, "r") as file:
                data = json.load(file)
                return {
                    "api_key": data.get("api_key"),
                    "base_url": data.get("base_url"),
                }
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"⚠️ Could not load API credentials: {e}")
                return None
    ```
    - This helper method tries to load API credentials from a JSON file
    - Opens the file and parses it as JSON
    - Extracts the "api_key" and "base_url" fields using `.get()` (which returns None if the key doesn't exist)
    - Returns a dictionary with these values
    - If the file isn't found or isn't valid JSON, prints an error and returns None
    - Shows proper error handling and use of type hints (`-> Optional[Dict[str, str]]`)

### Using Dialogue in Game
**File**: `level.py` (Lines 200-300)
- Shows how dialogue is triggered in the game
- Demonstrates NPC interaction systems

```python
    def player_attack_logic(self):
        """Handle player attack logic and NPC interactions."""
        if self.current_attack:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(
                    attack_sprite, self.attackable_sprites, False
                )
                if collision_sprites:
                    for target in collision_sprites:
                        if hasattr(target, 'get_status'):
                            target.get_damage(self, self.get_player_weapon_damage())
                        
                        # Check if the target is an NPC that can talk
                        if hasattr(target, 'trigger_dialogue'):
                            target.trigger_dialogue(self.dialogue_system)
```

**DETAILED WALKTHROUGH:**
This shows how we trigger dialogue when the player interacts with an NPC:

1. **Method Definition (Line 202)**:
   ```python
   def player_attack_logic(self):
   ```
   - Method that handles what happens when the player attacks

2. **Method Docstring (Lines 203-204)**:
   ```python
   """Handle player attack logic and NPC interactions."""
   ```
   - Explains what this method does

3. **Checking for Active Attack (Line 206)**:
   ```python
   if self.current_attack:
   ```
   - Only proceed if the player currently has an active attack (like a sword swing)

4. **Iterating Through Attack Sprites (Lines 207-208)**:
   ```python
   for attack_sprite in self.attack_sprites:
   ```
   - Loops through all sprites that are part of the current attack

5. **Collision Detection (Lines 209-213)**:
   ```python
   collision_sprites = pygame.sprite.spritecollide(
       attack_sprite, self.attackable_sprites, False
   )
   if collision_sprites:
   ```
   - Uses pygame's built-in sprite collision detection function
   - Checks if our attack sprite collides with any sprites in the attackable_sprites group
   - The `False` parameter means we don't automatically destroy the collided sprites
   - If there are collisions, we proceed to handle them

6. **Handling Each Collision (Lines 214-222)**:
   ```python
   for target in collision_sprites:
       if hasattr(target, 'get_status'):
           target.get_damage(self, self.get_player_weapon_damage())
       
       # Check if the target is an NPC that can talk
       if hasattr(target, 'trigger_dialogue'):
           target.trigger_dialogue(self.dialogue_system)
   ```
   - For each sprite we collided with:
   - First check if it has a `get_status` method (indicating it can take damage)
   - If so, call its `get_damage` method to apply damage from our attack
   - Then check if it has a `trigger_dialogue` method (indicating it's an NPC that can talk)
   - If so, call its `trigger_dialogue` method, passing in our dialogue system
   - This is a great example of duck typing in Python - we don't care what type of object it is, just whether it has the methods we need

### Example NPC Dialogue Trigger
**File**: `entities/npc.py` (if exists) or example from `player.py`
- Shows how NPCs can trigger dialogue

```python
class NPC(Entity):
    def __init__(self, pos, groups, obstacle_sprites, dialogue_system):
        super().__init__(groups)
        # ...existing code...
        self.dialogue_system = dialogue_system
        
    def trigger_dialogue(self, dialogue_system):
        """Trigger dialogue when interacted with."""
        # Example dialogue - in practice this would come from a data file
        dialogue_lines = [
            "Hello, traveler! Welcome to our village.",
            "Are you looking for work?",
            "I need help with my farm. Can you water the crops?",
            "Thank you! Here's a reward for your help."
        ]
        dialogue_system.set_dialogue(dialogue_lines)
```

**DETAILED WALKTHROUGH:**
This is an example of how an NPC might trigger dialogue:

1. **Class Definition (Line 1)**:
   ```python
   class NPC(Entity):
   ```
   - Our NPC class inherits from Entity (just like Player does)

2. **Constructor Method (Line 3)**:
   ```python
   def __init__(self, pos, groups, obstacle_sprites, dialogue_system):
       super().__init__(groups)
   ```
   - Takes the same parameters as Player, plus a dialogue_system reference
   - Calls the parent Entity constructor

3. **Storing Dialogue Reference (Line 6)**:
   ```python
   # ...existing code...
   self.dialogue_system = dialogue_system
   ```
   - Stores a reference to the dialogue system so we can use it later
   - The `...existing code...` placeholder indicates there's likely more initialization code here

4. **Dialogue Trigger Method (Line 9)**:
   ```python
   def trigger_dialogue(self, dialogue_system):
   ```
   - Method that gets called when the player interacts with this NPC
   - Interestingly, it takes a dialogue_system parameter, but we already stored one in `__init__`
   - In practice, we'd probably use the stored reference instead

5. **Method Docstring (Lines 10-11)**:
   ```python
   """Trigger dialogue when interacted with."""
   ```
   - Simple explanation

6. **Setting Up Dialogue (Lines 14-19)**:
   ```python
   # Example dialogue - in practice this would come from a data file
   dialogue_lines = [
       "Hello, traveler! Welcome to our village.",
       "Are you looking for work?",
       "I need help with my farm. Can you water the crops?",
       "Thank you! Here's a reward for your help."
   ]
   dialogue_system.set_dialogue(dialogue_lines)
   ```
   - Defines a list of dialogue lines (hardcoded for this example)
   - In a real game, this might come from a file or database
   - Calls the dialogue system's `set_dialogue` method to display these lines
   - Notice we're using the parameter `dialogue_system` here, but we could also use `self.dialogue_system`

## Key Learning Points
1. **Understanding how to store and manage dialogue data**
   - How lists are perfect for sequential dialogue lines
   - How we track our position in dialogue with an index variable
   - How we use boolean flags to track active/inactive states

2. **Using conditionals and loops for conversation flow**
   - How `if` statements check for input and state conditions
   - How we reset dialogue index when reaching the end
   - How loops process collections of dialogue lines or sprite collisions

3. **Integrating external APIs for dynamic content**
   - How we safely import optional dependencies (like openai)
   - How we handle missing dependencies gracefully with fallback modes
   - How we separate concerns between dialogue display and AI generation

4. **Creating interactive systems that respond to user input**
   - How we use pygame's input handling to detect key presses
   - How we implement debouncing to prevent input from being too sensitive
   - How we connect game mechanics (combat) to dialogue systems

5. **Organizing dialogue code in reusable modules**
   - How we separate dialogue logic into its own file
   - How we create specialized classes for different aspects (display vs AI)
   - How we use composition to connect systems together

## Extension Activities
1. Create a dialogue tree with at least 3 branches
   - Instead of just a list of lines, create a dictionary where keys represent dialogue states
   - Add logic to jump between different dialogue branches based on player choices
   - You might need to modify the input method to handle number keys for selecting options

2. Modify the dialogue system to show character portraits
   - Add a portrait image variable to the DialogueSystem class
   - Modify the draw method to blit the portrait next to the dialogue text
   - Create a method to set the portrait based on which NPC is speaking

3. Add a dialogue option that changes based on player inventory
   - Check what items the player has before setting dialogue
   - Show different dialogue options if the player has (or doesn't have) certain items
   - You'll need to access the player's inventory from the dialogue system

4. Implement a dialogue option that ends the conversation early
   - Add a special dialogue option like "Goodbye" or "Leave"
   - When selected, immediately set `self.active = False` to end the conversation
   - You might want to add a farewell message before ending

## Troubleshooting Tips
- If dialogue doesn't appear, check that the dialogue system is being updated in the game loop
  - Make sure you're calling `dialogue_system.input()` and `dialogue_system.draw()` in your main game loop
  - Verify that the dialogue system is being set to active when triggered
  
- Verify that the font file exists and is accessible
  - Check that "font/LycheeSoda.ttf" actually exists in your project
  - If not, either add the font file or change the path to a font you do have
  - You can also use a default pygame font with `pygame.font.Font(None, 30)`
  
- Ensure dialogue triggers are properly connected to NPC interactions
  - Verify that NPCs have the `trigger_dialogue` method
  - Check that the player's attack logic correctly identifies NPCs
  - Make sure the dialogue system is being passed to NPCs when they're created
  
- Check for errors in the AI API key configuration (if using AI features)
  - Verify that your API key file exists in the correct location
  - Make sure the JSON file has the correct format with "api_key" and "base_url" fields
  - Check that your API key is valid and hasn't expired
  - Look for console output that indicates whether AI initialization succeeded or fell back to offline mode