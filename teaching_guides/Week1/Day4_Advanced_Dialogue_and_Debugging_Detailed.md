# Day 4: Advanced Dialogue and Debugging

## Objective
Enhance dialogue systems, add sprite interactions, and learn debugging techniques.

## Core Concepts
- **Refining Dialogue Trees**
  - Multi-step dialogue structures
  - Explain this as the original "AI"
- **Sprite Interaction**
  - Tie sprite actions to dialogue choices
  - Change expressions based on conversation branches
  - Sprite movement (walking away, disappearing)
- **Basic Debugging & Code Organization**
  - Using `print()` statements to track variables
  - Common syntax errors and how to read error messages
  - Organizing dialogue code in separate files/functions

## Exercise: Complex Dialogue
- Create multi-branch dialogue for character
- **Optional**: Group brainstorming for final projects
- **Deliverable**: Push project to personal GitHub repository

## Code References

### Advanced Dialogue System
**File**: `dialogue_system.py` (Lines 200-300)
- Shows how to implement branching dialogue
- Demonstrates dialogue state management for complex conversations

```python
    def set_branching_dialogue(self, dialogue_tree):
        """Set up a branching dialogue structure."""
        self.dialogue_tree = dialogue_tree
        self.current_branch = "start"
        self.dialogue_index = 0
        self.active = True
        self._load_current_branch()
    
    def _load_current_branch(self):
        """Load the current dialogue branch for display."""
        if self.current_branch in self.dialogue_tree:
            self.current_dialogue = self.dialogue_tree[self.current_branch]
            self.dialogue_index = 0
        else:
            self.current_dialogue = ["...", "Let's talk later."]
            self.dialogue_index = 0
    
    def input(self):
        """Handle keyboard input for branching dialogue progression."""
        keys = pygame.key.get_just_pressed()
        
        if keys[pygame.K_SPACE] and not self.skip_next:
            self.dialogue_index += 1
            if self.dialogue_index >= len(self.current_dialogue):
                # End of current branch, check for branching options
                self._process_branch_options()
            else:
                self.dialogue_timer.activate()
        
        if keys[pygame.K_SPACE]:
            self.skip_next = True
        else:
            self.skip_next = False
    
    def _process_branch_options(self):
        """Process branching options at the end of dialogue."""
        # In a full implementation, this would present choices to the player
        # For now, we'll just end the dialogue or loop back
        self.active = False
        self.dialogue_index = 0
```

**DETAILED WALKTHROUGH:**
Let's examine our advanced dialogue system with branching capabilities:

1. **Setting Up Branching Dialogue (Lines 202-208)**:
   ```python
   def set_branching_dialogue(self, dialogue_tree):
       """Set up a branching dialogue structure."""
       self.dialogue_tree = dialogue_tree
       self.current_branch = "start"
       self.dialogue_index = 0
       self.active = True
       self._load_current_branch()
   ```
   - Instead of just a list of dialogue lines, we now accept a `dialogue_tree` parameter
   - A dialogue tree is typically a dictionary where keys are branch names and values are lists of dialogue lines
   - We store the entire tree in `self.dialogue_tree`
   - We start at the "start" branch (this would be the root of our conversation)
   - We reset our dialogue index to 0
   - We mark the dialogue as active
   - We call `_load_current_branch()` to load the initial dialogue lines

2. **Loading Current Branch (Lines 210-216)**:
   ```python
   def _load_current_branch(self):
       """Load the current dialogue branch for display."""
       if self.current_branch in self.dialogue_tree:
           self.current_dialogue = self.dialogue_tree[self.current_branch]
           self.dialogue_index = 0
       else:
           self.current_dialogue = ["...", "Let's talk later."]
           self.dialogue_index = 0
   ```
   - This helper method loads the dialogue lines for whatever branch we're currently on
   - It checks if our `current_branch` key exists in the dialogue tree dictionary
   - If it does, it sets `current_dialogue` to the list of lines for that branch
   - If it doesn't exist (maybe we made an error), it provides a fallback dialogue
   - In both cases, it resets the dialogue index to 0

3. **Input Handling for Branching Dialogue (Lines 218-234)**:
   ```python
   def input(self):
       """Handle keyboard input for branching dialogue progression."""
       keys = pygame.key.get_just_pressed()
       
       if keys[pygame.K_SPACE] and not self.skip_next:
           self.dialogue_index += 1
           if self.dialogue_index >= len(self.current_dialogue):
               # End of current branch, check for branching options
               self._process_branch_options()
           else:
               self.dialogue_timer.activate()
       
       if keys[pygame.K_SPACE]:
           self.skip_next = True
       else:
           self.skip_next = False
   ```
   - This is similar to our basic dialogue input, but with an important addition
   - When we reach the end of the current dialogue branch (`self.dialogue_index >= len(self.current_dialogue)`)...
   - Instead of just deactivating, we call `self._process_branch_options()` to handle what happens next
   - This is where we would present choices to the player in a full implementation

4. **Processing Branch Options (Lines 236-242)**:
   ```python
   def _process_branch_options(self):
       """Process branching options at the end of dialogue."""
       # In a full implementation, this would present choices to the player
       # For now, we'll just end the dialogue or loop back
       self.active = False
       self.dialogue_index = 0
   ```
   - Currently, this just ends the dialogue, but in a full implementation...
   - We would present the player with choices (like option A, option B, option C)
   - Based on their choice, we would set `self.current_branch` to a new value
   - Then we would call `self._load_current_branch()` to load the new dialogue lines
   - This is what creates the "branching" in dialogue trees - different paths based on player choices

### Sprite Interaction and Animation
**File**: `player.py` (Lines 100-200)
- Shows how to change sprite based on actions/dialogue
- Demonstrates animation state management

```python
    def animate(self, dt):
        """Animate the player sprite based on current status."""
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    def get_status(self):
        """Determine player status based on movement and actions."""
        # Movement status
        if self.direction.y < 0:
            self.status = 'up'
        elif self.direction.y > 0:
            self.status = 'down'
        elif self.direction.x < 0:
            self.status = 'left'
        elif self.direction.x > 0:
            self.status = 'right'
        else:
            # Idle status
            if self.status.split('_')[0] in ['up', 'down', 'left', 'right']:
                self.status = self.status.split('_')[0] + '_idle'
        
        # Attack status
        if self.attacking:
            if self.status.split('_')[0] in ['up', 'down', 'left', 'right']:
                self.status = self.status.split('_')[0] + '_attack'
```

**DETAILED WALKTHROUGH:**
This shows how we handle sprite animations based on the player's current state:

1. **Animation Method (Lines 102-110)**:
   ```python
   def animate(self, dt):
       """Animate the player sprite based on current status."""
       self.frame_index += self.animation_speed * dt
       if self.frame_index >= len(self.animations[self.status]):
           self.frame_index = 0
       
       self.image = self.animations[self.status][int(self.frame_index)]
       self.rect = self.image.get_rect(center = self.hitbox.center)
   ```
   - This method is called each frame to update the player's sprite image
   - Takes `dt` (delta time) as a parameter - the time since last frame
   - Increments `frame_index` by `animation_speed * dt` - this makes animation speed consistent regardless of frame rate
   - If we've gone past the last frame in our animation sequence, loop back to the first frame
   - Sets `self.image` to the current frame from our animations dictionary
   - Updates the rect to match the new image (important if different frames have different sizes)
   - Centers the rect on the hitbox so the sprite stays properly aligned

2. **Status Determination Method (Lines 112-126)**:
   ```python
   def get_status(self):
       """Determine player status based on movement and actions."""
       # Movement status
       if self.direction.y < 0:
           self.status = 'up'
       elif self.direction.y > 0:
           self.status = 'down'
       elif self.direction.x < 0:
           self.status = 'left'
       elif self.direction.x > 0:
           self.status = 'right'
       else:
           # Idle status
           if self.status.split('_')[0] in ['up', 'down', 'left', 'right']:
               self.status = self.status.split('_')[0] + '_idle'
       
       # Attack status
       if self.attacking:
           if self.status.split('_')[0] in ['up', 'down', 'left', 'right']:
               self.status = self.status.split('_')[0] + '_attack'
   ```
   - This method determines what animation state the player should be in
   - First checks vertical movement: if moving up/down, sets status accordingly
   - Then checks horizontal movement: if moving left/right, sets status accordingly
   - If not moving in either direction, sets an idle status based on the last direction faced
   - The `split('_')[0]` takes the direction part of a status like 'right_idle' and gets just 'right'
   - Finally, if the player is attacking, overrides the status to show the attack animation
   - This method is typically called in the update loop before animate()

### Dialogue-Driven Sprite Changes
**File**: `level.py` (Lines 250-350)
- Shows how dialogue choices can affect sprite behavior
- Demonstrates triggering animations based on conversation

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
                            # Store reference to target for dialogue callback
                            self.last_interacted_npc = target
                            target.trigger_dialogue(self.dialogue_system)
    
    def dialogue_callback(self, choice_index):
        """Handle dialogue choice callbacks."""
        if hasattr(self, 'last_interacted_npc') and self.last_interacted_npc:
            # Based on dialogue choice, make NPC react differently
            if choice_index == 0:  # Friendly choice
                self.last_interacted_npc.wave()  # Make NPC wave
                # Could also change NPC sprite to happy version
            elif choice_index == 1:  # Neutral choice
                pass  # No special reaction
            elif choice_index == 2:  # Unfriendly choice
                # Make NPC turn away or show angry expression
                pass
```

**DETAILED WALKTHROUGH:**
This shows how we connect dialogue choices to sprite behavior:

1. **Player Attack Logic (Lines 252-266)**:
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
                           # Store reference to target for dialogue callback
                           self.last_interacted_npc = target
                           target.trigger_dialogue(self.dialogue_system)
   ```
   - This is similar to what we saw before, but with an important addition
   - When we detect that we've hit an NPC that can talk...
   - We store a reference to that NPC in `self.last_interacted_npc`
   - Then we call `target.trigger_dialogue(self.dialogue_system)` to start the conversation
   - Storing the reference allows us to affect the NPC later based on dialogue choices

2. **Dialogue Callback Method (Lines 268-278)**:
   ```python
   def dialogue_callback(self, choice_index):
       """Handle dialogue choice callbacks."""
       if hasattr(self, 'last_interacted_npc') and self.last_interacted_npc:
           # Based on dialogue choice, make NPC react differently
           if choice_index == 0:  # Friendly choice
               self.last_interacted_npc.wave()  # Make NPC wave
               # Could also change NPC sprite to happy version
           elif choice_index == 1:  # Neutral choice
               pass  # No special reaction
           elif choice_index == 2:  # Unfriendly choice
               # Make NPC turn away or show angry expression
               pass
   ```
   - This method would be called when the player makes a choice in a branching dialogue
   - Takes `choice_index` as a parameter - which option the player selected
   - First checks if we have a record of the last NPC we interacted with
   - Then based on the choice index, we make the NPC react differently:
     - Choice 0 (Friendly): Make the NPC wave (calling a hypothetical `wave()` method)
     - Choice 1 (Neutral): Do nothing special
     - Choice 2 (Unfriendly): Make the NPC turn away or show angry expression
   - In a full implementation, we might:
     - Change the NPC's sprite to show different emotions
     - Make the NPC walk away or disappear
     - Give the player different rewards or consequences based on their choice

### Debugging Techniques
**File**: `main.py` (Lines 150-200)
- Shows how to use print statements for debugging
- Demonstrates tracking variables during gameplay

```python
    def run(self):
        """Main game loop."""
        while self.running:
            dt = self.clock.tick() / 1000  # Delta time in seconds
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.toggle_menu()
                    if event.key == pygame.K_c:
                        self.toggle_character_screen()
                    if event.key == pygame.K_e:  # Emotion detection key
                        self.emotion_detector.toggle_detection()
                    if event.key == pygame.K_d:  # Debug key
                        self.toggle_debug_mode()
            
            # Debug information
            if self.debug_mode:
                self.print_debug_info(dt)
            
            # Update game systems
            self.update(dt)
            
            # Draw everything
            self.draw()
            
            pygame.display.update()
    
    def toggle_debug_mode(self):
        """Toggle debug mode on/off."""
        self.debug_mode = not self.debug_mode
        print(f"Debug mode: {'ON' if self.debug_mode else 'OFF'}")
    
    def print_debug_info(self, dt):
        """Print debug information to console."""
        if hasattr(self.level, 'player') and self.level.player:
            player = self.level.player
            print(f"Player Pos: {player.rect.topleft}, "
                  f"Direction: {player.direction}, "
                  f"Status: {player.status}")
        
        if self.dialogue_system.active:
            print(f"Dialogue: {self.dialogue_system.current_dialogue[self.dialogue_system.dialogue_index] if self.dialogue_system.dialogue_index < len(self.dialogue_system.current_dialogue) else 'End'}")
```

**DETAILED WALKTHROUGH:**
This shows how we implement debugging capabilities in our game:

1. **Main Game Loop with Debugging (Lines 152-178)**:
   ```python
   def run(self):
       """Main game loop."""
       while self.running:
           dt = self.clock.tick() / 1000  # Delta time in seconds
           
           # Event handling
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running = False
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_m:
                       self.toggle_menu()
                   if event.key == pygame.K_c:
                       self.toggle_character_screen()
                   if event.key == pygame.K_e:  # Emotion detection key
                       self.emotion_detector.toggle_detection()
                   if event.key == pygame.K_d:  # Debug key
                       self.toggle_debug_mode()
           
           # Debug information
           if self.debug_mode:
               self.print_debug_info(dt)
           
           # Update game systems
           self.update(dt)
           
           # Draw everything
           self.draw()
           
           pygame.display.update()
   ```
   - We've added a new key binding: `if event.key == pygame.K_d:` to toggle debug mode
   - When debug mode is enabled (`if self.debug_mode:`), we call `self.print_debug_info(dt)` each frame
   - This shows how we can conditionally execute debugging code only when needed

2. **Toggle Debug Mode (Lines 180-183)**:
   ```python
   def toggle_debug_mode(self):
       """Toggle debug mode on/off."""
       self.debug_mode = not self.debug_mode
       print(f"Debug mode: {'ON' if self.debug_mode else 'OFF'}")
   ```
   - Simple method to flip the debug_mode boolean
   - Prints a message to the console showing the new state
   - This gives us immediate feedback when we press the debug key

3. **Print Debug Info (Lines 185-194)**:
   ```python
   def print_debug_info(self, dt):
       """Print debug information to console."""
       if hasattr(self.level, 'player') and self.level.player:
           player = self.level.player
           print(f"Player Pos: {player.rect.topleft}, "
                 f"Direction: {player.direction}, "
                 f"Status: {player.status}")
       
       if self.dialogue_system.active:
           print(f"Dialogue: {self.dialogue_system.current_dialogue[self.dialogue_system.dialogue_index] if self.dialogue_system.dialogue_index < len(self.dialogue_system.current_dialogue) else 'End'}")
   ```
   - This method prints useful debugging information to the console
   - First checks if we have a player object, then prints:
     - Player position (top-left corner of their rect)
     - Player direction vector (shows which way they're moving)
     - Player current animation status (like 'up', 'down_idle', 'right_attack')
   - Then checks if dialogue is active, and if so:
     - Prints the current line of dialogue being displayed
     - Uses a conditional expression to handle the case where we're between lines
   - This kind of debugging output is invaluable for understanding what's happening in your game

### Common Error Patterns
**File**: `support.py` (Lines 100-150)
- Shows how to handle common file loading errors
- Demonstrates graceful degradation

```python
def import_folder(path):
    surface_list = []
    
    try:
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
                try:
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)
                except pygame.error as e:
                    print(f"⚠️ Could not load image {full_path}: {e}")
                    # Add a placeholder surface
                    placeholder = pygame.Surface((32, 32))
                    placeholder.fill((255, 0, 255))  # Magenta for missing textures
                    surface_list.append(placeholder)
    except Exception as e:
        print(f"⚠️ Error accessing folder {path}: {e}")
    
    return surface_list
```

**DETAILED WALKTHROUGH:**
This shows how we've improved our image loading function to handle errors gracefully:

1. **Function Definition and Setup (Lines 102-104)**:
   ```python
   def import_folder(path):
       surface_list = []
   ```
   - Same as before - we're creating a function to load images from a folder

2. **Outer Try Block (Lines 106-122)**:
   ```python
   try:
       for _, __, img_files in walk(path):
           for image in img_files:
               full_path = path + '/' + image
               try:
                   image_surf = pygame.image.load(full_path).convert_alpha()
                   surface_list.append(image_surf)
               except pygame.error as e:
                   print(f"⚠️ Could not load image {full_path}: {e}")
                   # Add a placeholder surface
                   placeholder = pygame.Surface((32, 32))
                   placeholder.fill((255, 0, 255))  # Magenta for missing textures
                   surface_list.append(placeholder)
   except Exception as e:
       print(f"⚠️ Error accessing folder {path}: {e}")
   ```
   - We've wrapped the folder walking logic in a try-except block
   - This catches any errors that might occur when trying to access the folder itself
   - Inside the loop, we've added another try-except block specifically for loading each image
   - If `pygame.image.load()` fails for a particular image, we catch the `pygame.error`
   - We print a helpful warning message showing which file failed and why
   - Instead of crashing, we create a placeholder surface:
     - A 32x32 pixel surface
     - Filled with magenta color (255, 0, 255) - this makes missing textures obvious
   - We add this placeholder to our list so the game can continue running
   - If there's an error accessing the folder at all, we catch it in the outer except block
   - We print an error message but still return whatever surface_list we've managed to build

3. **Return Results (Line 124)**:
   ```python
   return surface_list
   ```
   - We return our list of surfaces, which may include placeholders for missing images
   - This allows the game to continue running even if some assets are missing or corrupted

## Key Learning Points
1. **Understanding how to create complex dialogue structures with branches**
   - How to represent dialogue as a tree structure using dictionaries
   - How to track current position in the dialogue tree
   - How to load different dialogue branches based on player choices
   - How to handle transitions between dialogue branches

2. **Using sprite animations and visual feedback to enhance interactions**
   - How to change sprite images based on character state (movement, attacking, etc.)
   - How to use delta time for frame-rate independent animation
   - How to organize animation frames in dictionaries for easy access
   - How to determine character status based on movement and action flags

3. **Implementing callback systems for dialogue choices to affect game state**
   - How to store references to game objects for later use
   - How to create callback functions that respond to player choices
   - How to make game characters react differently based on dialogue decisions
   - How to connect dialogue systems with game mechanics

4. **Applying debugging techniques to track variables and identify issues**
   - How to use toggleable debug modes to show/hide debugging information
   - What kinds of information are useful to display for debugging (position, direction, status)
   - How to conditionally execute debugging code only when needed
   - How to format debug output for readability

5. **Organizing code for maintainability and extensibility**
   - How to separate concerns into different methods and classes
   - How to use helper functions to reduce code duplication
   - How to design systems that can be easily extended (like adding new dialogue branches)
   - How to use composition to connect different game systems together

6. **Handling errors gracefully to prevent game crashes**
   - How to use try-except blocks to catch and handle errors
   - How to provide fallback behavior when resources are missing
   - How to log helpful error messages for debugging
   - How to continue game execution even when individual assets fail to load

## Extension Activities
1. Create a dialogue tree with at least 3 levels of branching
   - Instead of just linear dialogue, create a structure where choices lead to different conversations
   - For example: Greeting -> Ask about farm -> (Choice: Help with crops / Ask about family) -> Different outcomes
   - You'll need to modify the dialogue system to handle presenting choices and tracking selections

2. Add visual effects (particles, color changes) when dialogue choices are made
   - Create a particle system that emits sparkles or hearts when friendly choices are made
   - Change screen tint or add screen shake for dramatic choices
   - You'll need to create visual effect classes and integrate them with your dialogue callback system

3. Implement a dialogue system that remembers past conversations
   - Add a conversation history to your dialogue system
   - Make NPCs reference previous conversations in their dialogue
   - You might need to store dialogue state between game sessions

4. Create a debugging overlay that shows variables on screen
   - Instead of just printing to console, render debug information directly on the game screen
   - Create a debug mode that shows FPS, player coordinates, active systems, etc.
   - This is often more convenient than console debugging for real-time games

5. Add voice lines or sound effects that play with different dialogue options
   - Load sound effects for different dialogue choices
   - Play appropriate sounds when players make selections
   - You could even add different voice tones for different NPC personalities

## Troubleshooting Tips
- If dialogue doesn't branch correctly, check that your dialogue tree structure is properly formatted
  - Verify that your dialogue tree is a dictionary with string keys and list values
  - Make sure the branch names you're trying to access actually exist in the tree
  - Check that you're correctly setting and retrieving the current_branch variable
  
- Verify that sprite animations are being updated in the game loop
  - Make sure you're calling the animate() method in your update loop
  - Check that you're passing the correct delta time (dt) parameter
  - Ensure your animation_speed is set to a reasonable value (too fast = blinking, too slow = frozen)
  
- Ensure dialogue callbacks are properly connected to choice selections
  - Verify that your dialogue system is calling the callback function when choices are made
  - Check that the callback function is receiving the correct choice_index parameter
  - Make sure any methods you're calling on game objects (like wave()) actually exist
  
- Check for infinite loops in dialogue processing logic
  - Make sure your dialogue advancement logic has proper exit conditions
  - Verify that you're not accidentally setting dialogue_index to create an infinite loop
  - Check that branch transitions eventually lead to an ending state
  
- Look for undefined variables when accessing dialogue choice results
  - Verify that all variables you're accessing in your callback methods actually exist
  - Check that you're not trying to access attributes on None objects
  - Make sure you're properly checking for object existence before using them
  
- Verify that all required image files exist for sprite animations
  - Check that all the animation frames referenced in your code actually exist on disk
  - Make sure you're using the correct file paths and extensions
  - Consider adding error handling to your image loading functions (like we did in support.py)