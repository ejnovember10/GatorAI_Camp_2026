# Day 4: Game Integration - Facial Recognition + LLM

## Objective
Combine facial recognition and LLM technologies in the game.

## Core Concepts
- **Loading Facial Recognition Model**
  - Load saved model from Day 2 into game code
  - Integrate webcam/image capture for real-time analysis
  - Snapshot-based approach (keypress to check expression)
- **API Calls from In-Game**
  - Combine LLM API script with game logic
  - Dynamic prompts based on recognized expressions
  - Example: "User is smiling. NPC responds with friendly greeting."
- **Designing Interaction Flow**
  - Craft LLM prompts with contextual info
  - Map expressions to conversation branches (happy → friendly, sad → consoling)
- **Error Handling & Debugging**
  - Handle API downtime or recognition failures
  - Use `print()` statements for debugging

## Hands-On Exercise
- Incorporate model + LLM calls into game dialogue function
- Group testing: one person as "player" (webcam), other monitors code

## Code References

### Emotion Detector Integration
**File**: `main.py` (Lines 300-350)
- Shows how emotion detection is initialized and used in the main game
- Demonstrates toggling emotion detection and storing results

```python
    def __init__(self):
        # ...existing code...
        # Initialize emotion detector
        self.emotion_detector = EmotionDetector()
        self.current_emotion = None
        self.current_emotion_confidence = 0.0
        # ...existing code...
```

**File**: `main.py` (Lines 350-400)
- Shows how emotion detection is toggled and updated
- Demonstrates using emotion data to influence game systems

```python
    def toggle_emotion_detection(self):
        """Toggle emotion detection on/off."""
        if self.emotion_detector.is_running:
            self.emotion_detector.stop_detection()
            print("🛑 Emotion detection stopped")
        else:
            if self.emotion_detector.start_detection():
                print("📹 Emotion detection started")
            else:
                print("⚠️ Failed to start emotion detection")
    
    def update(self, dt):
        """Update game systems."""
        self.level.update(dt)
        
        # Update emotion detection if active
        if self.emotion_detector.is_running:
            emotion, confidence = self.emotion_detector.get_emotion()
            # Store current emotion for dialogue system
            if emotion not in ["not_running", "no_face", "error"] and confidence > 0.5:
                self.current_emotion = emotion
                self.current_emotion_confidence = confidence
            else:
                self.current_emotion = None
        
        # Update dialogue system
        self.dialogue_system.update(dt)
```

### LLM Integration with Emotion Context
**File**: `dialogue_system.py` (Lines 250-350)
- Shows how to set AI dialogue with emotional context
- Demonstrates updating dialogue based on detected emotions

```python
    def set_ai_dialogue_with_emotion(self, base_prompt: str = ""):
        """Set dialogue using AI generation with emotional context."""
        emotion_context = ""
        if hasattr(self.game, 'current_emotion') and self.game.current_emotion:
            emotion_context = self.game.current_emotion
            confidence = getattr(self.game, 'current_emotion_confidence', 0.0)
            # Only use emotion if confidence is high enough
            if confidence < 0.5:
                emotion_context = ""
        
        if self.ai_manager and not self.ai_manager.fallback_mode:
            ai_dialogue = self.ai_manager.generate_dialogue_with_context(
                base_prompt, emotion_context
            )
            # Split into lines for display
            dialogue_lines = [line.strip() for line in ai_dialogue.split('.') if line.strip()]
            self.set_dialogue(dialogue_lines)
        else:
            # Fallback to predefined dialogue with emotion awareness
            fallback_dialogue = self.ai_manager._fallback_dialogue_with_emotion(
                base_prompt, emotion_context
            )
            dialogue_lines = [line.strip() for line in fallback_dialogue.split('.') if line.strip()]
            self.set_dialogue(dialogue_lines)
```

### NPC Interaction with Emotion-Aware Dialogue
**File**: `level.py` (Lines 350-450)
- Shows how NPCs use emotion-aware dialogue when interacted with
- Demonstrates passing emotion context to dialogue system

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
                            # Pass the game reference so NPC can access emotion data
                            target.trigger_dialogue(self.dialogue_system, self.game)
```

**File**: `entities/npc.py` (example implementation)
- Shows how NPCs trigger emotion-aware dialogue

```python
class NPC(Entity):
    def __init__(self, pos, groups, obstacle_sprites, dialogue_system):
        super().__init__(groups)
        # ...existing code...
        self.dialogue_system = dialogue_system
        
    def trigger_dialogue(self, dialogue_system, game=None):
        """Trigger dialogue when interacted with, using emotion context if available."""
        # Base dialogue prompt
        base_prompt = "Greet the player and offer help with farming tasks"
        
        # If we have access to the game and emotion detector, use emotion-aware dialogue
        if game and hasattr(dialogue_system, 'set_ai_dialogue_with_emotion'):
            dialogue_system.game = game  # Pass game reference for emotion access
            dialogue_system.set_ai_dialogue_with_emotion(base_prompt)
        else:
            # Fallback to predefined dialogue
            dialogue_lines = [
                "Hello, traveler! Welcome to our village.",
                "Are you looking for work?",
                "I need help with my farm. Can you water the crops?",
                "Thank you! Here's a reward for your help."
            ]
            dialogue_system.set_dialogue(dialogue_lines)
```

### Debugging and Error Handling
**File**: `main.py` (Lines 400-450)
- Shows how to add debugging information for AI systems
- Demonstrates error handling and fallback notifications

```python
    def draw(self):
        """Draw all game elements."""
        self.display_surface.fill(WATER_COLOR)
        self.level.draw()
        
        # Draw UI elements
        self.main_menu.draw()
        self.character_screen.draw()
        
        # Draw emotion detection status
        if self.emotion_detector.is_running:
            emotion_text = f"Emotion: {self.current_emotion or 'Detecting...'}"
            if self.current_emotion_confidence > 0:
                emotion_text += f" ({self.current_emotion_confidence:.2f})"
            # In a full implementation, this would be rendered on screen
            print(emotion_text)  # Debug output
        
        # Draw dialogue system
        self.dialogue_system.draw()
```

## Key Learning Points
1. How to integrate multiple AI systems (computer vision + NLP) into a single application
2. Using real-time data (emotion detection) to influence AI-generated content
3. Designing context-aware prompts for better AI responses
4. Implementing graceful fallbacks when AI systems fail or are unavailable
5. Debugging AI integrations and monitoring system performance
6. Creating engaging user experiences that respond to player emotions

## Extension Activities
1. Create different NPC personalities that respond differently to the same emotions
2. Add memory to the dialogue system so NPCs remember previous conversations
3. Implement emotion-based gameplay mechanics (e.g., happy players get better prices)
4. Create a visualization of emotion detection results within the game UI
5. Experiment with different emotion-to-dialogue mapping strategies

## Troubleshooting Tips
- If emotion detection isn't working, verify the webcam is functioning and properly connected
- Check that the emotion model file exists and is in the correct format
- If AI dialogue isn't generating, verify API key configuration and internet connectivity
- Look for performance issues when running both AI systems simultaneously
- Ensure that emotion data is being properly passed between game systems
- Check for threading issues if implementing real-time emotion detection