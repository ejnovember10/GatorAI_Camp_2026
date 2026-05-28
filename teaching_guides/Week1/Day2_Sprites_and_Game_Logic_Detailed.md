# Day 2: Sprites and Game Logic

## Objective
Explore game mechanics and make active changes to game code.

## Core Concepts
- **Loading Character Sprites**
  - Import image files (PNGs, JPGs) into game code
  - Position sprites on screen
- **Basic Conditionals**
  - `if` statements for simple conditions
  - Examples: button presses, health checks
- **Simple Functions**
  - Create functions like `move_character()` 
  - Demonstrate code organization benefits

## Exercise: Adding Your First Character
- Add a single character sprite to the game
- Use [Piskel](https://www.piskelapp.com/) to create unique sprites
- Experiment with character position and appearance
- **Deliverable**: Push project to personal GitHub repository

## Code References

### Sprite Loading and Rendering
**File**: `level.py` (Lines 1-50)
- Shows how the game loads and renders sprites
- Demonstrates sprite groups and rendering order

```python
"""
Level Management - Handles Game World and Sprites
=================================================
This file manages the game world, including:
- Loading and rendering tile maps
- Managing sprite groups for different game elements
- Handling collisions and interactions
"""

import pygame
import pytmx
from pytmx.util_pygame import load_pygame
from settings import *
from support import *
from entity import Entity

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # Attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        
        self.setup_level()
```

**DETAILED WALKTHROUGH:**
Let's break down what's happening in this level initialization code:

1. **Module Docstring (Lines 1-8)**:
   ```python
   """
   Level Management - Handles Game World and Sprites
   =================================================
   This file manages the game world, including:
   - Loading and rendering tile maps
   - Managing sprite groups for different game elements
   - Handling collisions and interactions
   """
   ```
   - This docstring explains the purpose of the level.py file
   - It tells us this file handles the game world, which includes the map, sprites, collisions, etc.

2. **Imports (Lines 11-15)**:
   ```python
   import pygame
   import pytmx
   from pytmx.util_pygame import load_pygame
   from settings import *
   from support import *
   from entity import Entity
   ```
   - `pygame`: Our main game library
   - `pytmx`: A library for loading Tiled map editor files (.tmx)
   - `from pytmx.util_pygame import load_pygame`: A specific function from pytmx that makes it easier to work with pygame
   - `from settings import *`: All our game configuration constants
   - `from support import *`: Helper functions we've created (like importing folders of images)
   - `from entity import Entity`: The base Entity class that our player and enemies will inherit from

3. **Class Definition (Line 18)**:
   ```python
   class Level:
   ```
   - This defines our Level class that will manage the game world

4. **Constructor Method (Line 20)**:
   ```python
   def __init__(self):
   ```
   - The constructor that runs when we create a new Level object

5. **Getting Display Surface (Line 23)**:
   ```python
   # Get the display surface
   self.display_surface = pygame.display.get_surface()
   ```
   - Instead of creating a new display, we're getting the one that was already created in our Game class
   - `pygame.display.get_surface()` returns the main display surface we set up earlier
   - We store it in `self.display_surface` so we can draw to it later

6. **Sprite Groups (Lines 26-30)**:
   ```python
   # Sprite groups
   self.visible_sprites = YSortCameraGroup()
   self.obstacle_sprites = pygame.sprite.Group()
   
   # Attack sprites
   self.current_attack = None
   self.attack_sprites = pygame.sprite.Group()
   self.attackable_sprites = pygame.sprite.Group()
   ```
   - We're creating different groups to organize our sprites:
     - `visible_sprites`: All sprites that should be drawn on screen (using a custom YSortCameraGroup for proper drawing order)
     - `obstacle_sprites`: Sprites that the player can't walk through (like walls, trees)
     - `attack_sprites`: Currently active attack (like a sword swing)
     - `attackable_sprites`: Sprites that can be damaged by attacks (like enemies, breakable objects)
   - Using sprite groups is a pygame best practice for managing many sprites efficiently

7. **Setup Method Call (Line 34)**:
   ```python
   self.setup_level()
   ```
   - This calls a method that will actually load our game level (we'd see this method if we looked at more lines)

### Support Functions for Loading Images
**File**: `support.py` (Lines 1-50)
- Shows utility functions for loading images and assets
- Demonstrates how to import and scale sprites

```python
"""
Support Functions - Utility helpers for game development
=======================================================
This file contains helper functions used throughout the game:
- Importing folders of images
- Loading and scaling sprites
- Audio management
"""

import pygame
from os import walk
import os

def import_folder(path):
    surface_list = []
    
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
            
    return surface_list
```

**DETAILED WALKTHROUGH:**
This is a helper function that makes it easy to load multiple images from a folder:

1. **Module Docstring (Lines 1-8)**:
   ```python
   """
   Support Functions - Utility helpers for game development
   =======================================================
   This file contains helper functions used throughout the game:
   - Importing folders of images
   - Loading and scaling sprites
   - Audio management
   """
   ```
   - Explains what this file contains - reusable helper functions

2. **Imports (Lines 11-13)**:
   ```python
   import pygame
   from os import walk
   import os
   ```
   - `pygame`: For loading and working with images
   - `from os import walk`: A function to recursively walk through directories
   - `import os`: For general operating system interactions

3. **Function Definition (Line 16)**:
   ```python
   def import_folder(path):
   ```
   - A function that takes a folder path and returns a list of loaded images

4. **Initialize Result List (Line 18)**:
   ```python
   surface_list = []
   ```
   - We'll store our loaded images in this list

5. **Walk Through Directory (Lines 20-23)**:
   ```python
   for _, __, img_files in walk(path):
       for image in img_files:
           full_path = path + '/' + image
           image_surf = pygame.image.load(full_path).convert_alpha()
           surface_list.append(image_surf)
   ```
   - `walk(path)` recursively goes through the directory and all subdirectories
   - For each directory it visits, it gives us `(dirpath, dirnames, filenames)`
   - We only care about the filenames (`img_files`), so we use `_` for the other two
   - For each image file, we:
     - Construct the full file path
     - Load the image with `pygame.image.load()`
     - Convert it for efficient pygame use with `.convert_alpha()` (preserves transparency)
     - Add it to our list

6. **Return Results (Line 27)**:
   ```python
   return surface_list
   ```
   - Give back the list of all loaded images

### Basic Conditionals and Functions
**File**: `player.py` (Lines 1-50)
- Shows player movement and input handling
- Demonstrates basic conditionals for key presses
- Illustrates function organization for game logic

```python
"""
Player Entity - Handles Player Character Logic
=============================================
This file manages the player character, including:
- Movement and animation
- Input handling
- Combat and interactions
"""

import pygame
from settings import *
from support import *
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/character/down/down_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET['player'])
        
        # Graphics setup
        self.import_player_assets()
        self.status = 'down'
        
    def import_player_assets(self):
        character_path = 'graphics/character/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_attack':[], 'left_attack':[], 'up_attack':[], 'down_attack':[]}
        
        for animation in self.animations:
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
```

**DETAILED WALKTHROUGH:**
This is where we define our Player class:

1. **Module Docstring (Lines 1-8)**:
   ```python
   """
   Player Entity - Handles Player Character Logic
   =============================================
   This file manages the player character, including:
   - Movement and animation
   - Input handling
   - Combat and interactions
   """
   ```
   - Explains what this file does

2. **Imports (Lines 11-14)**:
   ```python
   import pygame
   from settings import *
   from support import *
   from entity import Entity
   ```
   - Standard imports for our game

3. **Class Definition (Line 17)**:
   ```python
   class Player(Entity):
   ```
   - Our Player class inherits from Entity (which we saw earlier)
   - This means Player gets all the functionality of Entity, plus we can add player-specific features

4. **Constructor Method (Line 19)**:
   ```python
   def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack):
   ```
   - Takes several parameters:
     - `pos`: Starting position (x, y) for the player
     - `groups`: Sprite groups the player should belong to
     - `obstacle_sprites`: Reference to obstacle sprites for collision detection
     - `create_attack` and `destroy_attack`: Callback functions for creating/destroying attacks

5. **Parent Constructor Call (Line 21)**:
   ```python
   super().__init__(groups)
   ```
   - Calls the parent class (Entity) constructor
   - Passes along the groups parameter

6. **Player Sprite Setup (Lines 24-26)**:
   ```python
   self.image = pygame.image.load('graphics/character/down/down_idle.png').convert_alpha()
   self.rect = self.image.get_rect(topleft = pos)
   self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET['player'])
   ```
   - Loads the player's default sprite (facing down, idle)
   - Gets the rectangle that defines the sprite's position and size
   - Creates a hitbox that's slightly smaller than the visual rect for better collision detection
   - `HITBOX_OFFSET['player']` comes from settings.py

7. **Graphics Setup (Lines 29-30)**:
   ```python
   # Graphics setup
   self.import_player_assets()
   self.status = 'down'
   ```
   - Loads all the player's animation frames
   - Sets initial status to 'down' (facing down)

8. **Asset Importing Method (Lines 33-42)**:
   ```python
   def import_player_assets(self):
       character_path = 'graphics/character/'
       self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                          'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                          'right_attack':[], 'left_attack':[], 'up_attack':[], 'down_attack':[]}
       
       for animation in self.animations:
           full_path = character_path + animation
           self.animations[animation] = import_folder(full_path)
   ```
   - Creates a dictionary to hold all our animation frames
   - For each direction and action (up, down, left, right, and their idle/attack variants)
   - Loads all images from the corresponding folder using our `import_folder` helper
   - This gives us a dictionary where we can access animations like `self.animations['up']` to get all the upward-facing frames

### Entity Base Class with Movement Logic
**File**: `entity.py` (Lines 1-50)
- Shows base entity class with movement logic
- Demonstrates how conditionals control sprite behavior

```python
"""
Entity Base Class - Shared functionality for game characters
===========================================================
This file contains the base Entity class that both Player and Enemy inherit from:
- Movement and collision handling
- Animation framework
- Basic game object properties
"""

import pygame
from settings import *
from support import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
```

**DETAILED WALKTHROUGH:**
This is the base class that both Player and Enemy inherit from:

1. **Module Docstring (Lines 1-8)**:
   ```python
   """
   Entity Base Class - Shared functionality for game characters
   ===========================================================
   This file contains the base Entity class that both Player and Enemy inherit from:
   - Movement and collision handling
   - Animation framework
   - Basic game object properties
   """
   ```
   - Explains what this file contains

2. **Imports (Lines 11-13)**:
   ```python
   import pygame
   from settings import *
   from support import *
   ```
   - Standard game imports

3. **Class Definition (Line 16)**:
   ```python
   class Entity(pygame.sprite.Sprite):
   ```
   - Our Entity class inherits from pygame.sprite.Sprite
   - This gives it built-in sprite functionality from pygame

4. **Constructor Method (Line 18)**:
   ```python
   def __init__(self, groups):
       super().__init__(groups)
   ```
   - Simple constructor that just calls the parent Sprite constructor with the groups

5. **Movement Method (Lines 21-30)**:
   ```python
   def move(self, speed):
       if self.direction.magnitude() != 0:
           self.direction = self.direction.normalize()
           
       self.hitbox.x += self.direction.x * speed
       self.collision('horizontal')
       self.hitbox.y += self.direction.y * speed
       self.collision('vertical')
       self.rect.center = self.hitbox.center
   ```
   - This is where movement happens! Let's break it down:
   - Takes a `speed` parameter (how fast to move)
   - First checks if we're actually moving (`self.direction.magnitude() != 0`)
   - If we are moving, normalizes the direction vector (makes it length 1 so diagonal movement isn't faster)
   - Moves the hitbox horizontally by `direction.x * speed`
   - Checks for horizontal collisions
   - Moves the hitbox vertically by `direction.y * speed`
   - Checks for vertical collisions
   - Updates the visual rect to match the hitbox position

6. **Collision Handling (Lines 33-46)**:
   ```python
   def collision(self, direction):
       if direction == 'horizontal':
           for sprite in self.obstacle_sprites:
               if sprite.hitbox.colliderect(self.hitbox):
                   if self.direction.x > 0: # moving right
                       self.hitbox.right = sprite.hitbox.left
                   if self.direction.x < 0: # moving left
                       self.hitbox.left = sprite.hitbox.right
                           
       if direction == 'vertical':
           for sprite in self.obstacle_sprites:
               if sprite.hitbox.colliderect(self.hitbox):
                   if self.direction.y > 0: # moving down
                       self.hitbox.bottom = sprite.hitbox.top
                   if self.direction.y < 0: # moving up
                       self.hitbox.top = sprite.hitbox.bottom
   ```
   - This handles what happens when we hit an obstacle
   - Separates horizontal and vertical collision checking (important for sliding along walls)
   - For each obstacle sprite, checks if our hitbox overlaps with theirs
   - If so, adjusts our position to be just outside the obstacle
   - The comments show which direction we're moving from

## Key Learning Points
1. **Understanding how games load and display images (sprites)**
   - How pygame loads image files from disk
   - Why we use `convert_alpha()` for better performance and transparency
   - How we organize animations in dictionaries by direction/action

2. **Working with coordinate systems for sprite positioning**
   - How pygame uses a coordinate system where (0,0) is top-left
   - The difference between visual rect and collision hitbox
   - How we update position based on direction and speed

3. **Using conditionals to respond to user input**
   - How `if` statements check for movement directions
   - How we normalize vectors to prevent faster diagonal movement
   - How collision detection prevents sprites from walking through walls

4. **Creating reusable functions for game logic**
   - How we separate concerns (movement vs collision vs rendering)
   - How helper functions like `import_folder` reduce code duplication
   - How inheritance lets us share common functionality between Player and Enemy

5. **Organizing code with classes and inheritance**
   - How Entity provides shared functionality for all game characters
   - How Player extends Entity with player-specific features
   - How we use composition (sprite groups) to manage collections of objects

## Extension Activities
1. Modify the player sprite to use a different direction (up, left, right)
   - Look in `player.py` where `self.status` is set
   - Try changing `'down'` to `'up'`, `'left'`, or `'right'`
   - You'll need to make sure those animations exist in your graphics folder

2. Change the player's movement speed by adjusting constants
   - Find where speed is used in the `move` method
   - Look for speed constants in settings.py (like PLAYER_SPEED)
   - Try different values and see how it feels

3. Add a simple boundary check to prevent the player from leaving the screen
   - In the `move` method, after updating position, check if the player is outside screen bounds
   - If so, move them back inside
   - You'll need to access screen dimensions from settings.py

4. Create a function that makes the player sprite blink or change color
   - Add a timer that periodically changes the player's image
   - Or create a white flash effect when taking damage
   - This would involve modifying the update/draw methods

## Troubleshooting Tips
- If sprites don't appear, check file paths and image formats
  - Make sure the path in `pygame.image.load()` matches your actual file structure
  - Verify that image files are actually in the directories you're pointing to
  - Check that you're using supported formats (PNG with transparency works best)
  
- Ensure pygame is properly initialized before loading images
  - Remember that `pygame.init()` must be called before any pygame functions
  - In our game, this happens in the Game class constructor
  
- Verify that sprite groups are being updated and drawn in the game loop
  - Check that you're calling `update()` and `draw()` on your sprite groups
  - Make sure these calls happen in your main game loop
  
- Check for indentation errors in conditional statements
  - Python is very sensitive to indentation
  - Make sure all code inside an `if` statement is indented consistently
  - Use spaces (not tabs) for indentation, and be consistent (usually 4 spaces)