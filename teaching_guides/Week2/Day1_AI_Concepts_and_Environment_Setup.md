# Day 1: AI Concepts and Environment Setup

## Objective
Learn AI fundamentals and prepare development environment.

## Core Concepts
- **Show Week Plan**: Overview of full week schedule
- **What Is AI/ML?**
  - Differentiate AI, Machine Learning, and Deep Learning
  - Real-world applications (image recognition, chatbots, etc.)
- **Facial Recognition Overview**
  - Face detection vs. recognition vs. expression recognition
  - Introduction to libraries (OpenCV, face_recognition)
- **Setting Up AI Environment**
  - Install Python libraries (`opencv-python`, `face_recognition`)
  - Discuss CPU/GPU considerations or use Google Colab
- **Data Gathering & Model Training Basics**
  - Using images/webcam for training/fine-tuning
  - Dataset labeling, data requirements
  - **Ethical considerations**: privacy, consent

## Hands-On Exercise
- Verify AI library installations (`pip install opencv-python`)
- **Optional**: Test script for face detection from webcam/image

## Code References

### Emotion Detector Implementation
**File**: `emotion_detector.py` (Lines 1-50)
- Shows how facial recognition is implemented in the game
- Demonstrates OpenCV usage for face detection

```python
"""
Emotion Detector - Facial Recognition for Game Integration
=========================================================
This module handles facial recognition and emotion detection using OpenCV.
It can be used to detect player expressions and influence game dialogue.

Educational Concepts Covered:
- Computer vision with OpenCV
- Face detection and recognition
- Real-time video processing
- Model loading and inference
- Integration with game systems
"""

import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

class EmotionDetector:
    def __init__(self):
        """Initialize the emotion detector with face cascade and emotion model."""
        # Load face detection cascade
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        # Load emotion recognition model
        model_path = "ai_materials/emotion_model.pth"
        if os.path.exists(model_path):
            try:
                self.emotion_model = load_model(model_path)
                self.model_loaded = True
            except Exception as e:
                print(f"⚠️ Could not load emotion model: {e}")
                self.emotion_model = None
                self.model_loaded = False
        else:
            print(f"⚠️ Emotion model not found at {model_path}")
            self.emotion_model = None
            self.model_loaded = False
            
        # Emotion labels
        self.emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        
        # Video capture
        self.video_capture = None
        self.is_running = False
```

### AI Dialogue Manager (continued)
**File**: `ai_dialogue_manager.py` (Lines 50-150)
- Shows how AI dialogue generation works
- Demonstrates prompt engineering and response handling

```python
    def generate_dialogue(self, prompt: str, context: str = "", max_tokens: int = 150) -> str:
        """Generate dialogue using the AI API or fallback to predefined responses."""
        if self.fallback_mode or self.client is None:
            return self._fallback_dialogue(prompt, context)
        
        try:
            # Construct the full prompt with context
            full_prompt = f"{context}\n{prompt}" if context else prompt
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a friendly NPC in a farming adventure game. Keep responses short, in-character, and helpful."},
                    {"role": "user", "content": full_prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7,
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ AI API error: {e}")
            return self._fallback_dialogue(prompt, context)
    
    def _fallback_dialogue(self, prompt: str, context: str = "") -> str:
        """Provide fallback dialogue when AI is not available."""
        fallback_responses = [
            "Hello there! How can I help you today?",
            "That's interesting! Tell me more.",
            "I'm not sure I understand. Could you rephrase that?",
            "Thanks for sharing! Have a great day!",
            "Sorry, I'm having trouble thinking right now. Come back later?",
            "Wow! That's amazing! I wish I could do that too.",
            "Hmm, let me think about that...",
            "I appreciate you saying that. It means a lot.",
        ]
        import random
        return random.choice(fallback_responses)
```

### Integration in Game Systems
**File**: `main.py` (Lines 100-200)
- Shows how AI systems are integrated into the main game loop
- Demonstrates emotion detection and dialogue generation integration

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
            
            # Update game systems
            self.update(dt)
            
            # Draw everything
            self.draw()
            
            pygame.display.update()
```

## Key Learning Points
1. Understanding the difference between AI, ML, and DL
2. How computer vision works for face detection
3. Using pre-trained models for emotion recognition
4. Integrating AI APIs for dynamic content generation
5. Ethical considerations in AI development
6. How to handle AI service failures gracefully

## Extension Activities
1. Modify the emotion detector to recognize additional emotions
2. Create a script that uses the webcam to detect faces in real-time
3. Experiment with different prompts for the AI dialogue system
4. Add a confidence threshold to the emotion detection
5. Create a visualization of emotion detection results

## Troubleshooting Tips
- If OpenCV fails to load, check that opencv-python is properly installed
- Verify the emotion model file exists in the correct location
- Ensure webcam permissions are granted for emotion detection
- Check API key configuration if using AI dialogue features
- Look for version compatibility issues between TensorFlow/Keras and OpenCV