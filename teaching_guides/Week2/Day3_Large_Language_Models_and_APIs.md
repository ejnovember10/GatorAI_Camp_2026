# Day 3: Large Language Models and APIs

## Objective
Understand LLMs and integrate them via API calls.

## Core Concepts
- **Overview of Large Language Models (LLMs)**
  - What LLMs are and how they're trained
  - Natural language response capabilities
  - Common providers (OpenAI, Hugging Face, etc.)
- **API Setup**
  - Obtain API keys (instructor-guided)
  - Basic Python script for LLM endpoint requests
  - Using `requests` library or official client libraries
- **Handling LLM Responses**
  - Parse JSON/text responses
  - Understanding token usage and limits

## Hands-On Exercise
- Write Python script to send prompts to LLM
- Print console responses
- Generate dialogue lines or short stories
- Use original dialogue as context pre-prompts

## Code References

### AI Dialogue Manager (continued)
**File**: `ai_dialogue_manager.py` (Lines 100-200)
- Shows how to generate dialogue with LLMs
- Demonstrates error handling and fallback mechanisms

```python
    def generate_dialogue_with_context(self, prompt: str, emotion_context: str = "", max_tokens: int = 150) -> str:
        """Generate dialogue with emotional context for more personalized responses."""
        if self.fallback_mode or self.client is None:
            return self._fallback_dialogue_with_emotion(prompt, emotion_context)
        
        try:
            # Construct prompt with emotional context
            if emotion_context:
                full_prompt = f"The user is currently feeling {emotion_context}. {prompt}"
            else:
                full_prompt = prompt
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a friendly NPC in a farming adventure game. Respond naturally to the user's emotions and keep responses concise and in-character."},
                    {"role": "user", "content": full_prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7,
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"⚠️ AI API error: {e}")
            return self._fallback_dialogue_with_emotion(prompt, emotion_context)
    
    def _fallback_dialogue_with_emotion(self, prompt: str, emotion_context: str = "") -> str:
        """Provide fallback dialogue with emotional awareness."""
        emotion_responses = {
            'happy': [
                "Your smile is contagious! What's making you so happy today?",
                "I love seeing you happy! How can I help make your day even better?",
                "That's wonderful to hear! Happiness looks good on you."
            ],
            'sad': [
                "I notice you seem down. Would you like to talk about what's bothering you?",
                "Sending you positive vibes. Sometimes talking helps when we're feeling sad.",
                "It's okay to feel sad sometimes. I'm here if you need someone to listen."
            ],
            'angry': [
                "I sense you're frustrated. Take a deep breath - want to talk about what's upsetting you?",
                "It sounds like something's really bothering you. I'm here to listen without judgment.",
                "Let's try to work through this together. What's on your mind?"
            ],
            'neutral': [
                "Hello there! How's your day going?",
                "Nice to see you! What brings you to our village today?",
                "Greetings! Is there something I can help you with?"
            ]
        }
        
        # Select response based on emotion, or use general fallback
        if emotion_context in emotion_responses:
            import random
            return random.choice(emotion_responses[emotion_context])
        else:
            return self._fallback_dialogue(prompt)
```

### Integration with Game Systems
**File**: `main.py` (Lines 250-300)
- Shows how LLM-generated dialogue is used in the game
- Demonstrates combining emotion detection with AI dialogue

```python
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

**File**: `dialogue_system.py` (Lines 150-250)
- Shows how the dialogue system uses AI-generated content
- Demonstrates updating dialogue with emotional context

```python
    def update(self, dt):
        """Update the dialogue system."""
        self.dialogue_timer.update()
        
        # Update AI-generated dialogue if needed
        if self.active and self.ai_manager and not self.fallback_mode:
            # Could regenerate dialogue based on current game state or emotions
            pass
    
    def set_ai_dialogue(self, prompt: str, emotion_context: str = ""):
        """Set dialogue using AI generation."""
        if self.ai_manager and not self.ai_manager.fallback_mode:
            ai_dialogue = self.ai_manager.generate_dialogue_with_context(
                prompt, emotion_context
            )
            # Split into lines for display
            dialogue_lines = [line.strip() for line in ai_dialogue.split('.') if line.strip()]
            self.set_dialogue(dialogue_lines)
        else:
            # Fallback to predefined dialogue
            fallback_dialogue = self.ai_manager._fallback_dialogue_with_emotion(
                prompt, emotion_context
            )
            dialogue_lines = [line.strip() for line in fallback_dialogue.split('.') if line.strip()]
            self.set_dialogue(dialogue_lines)
```

### Testing LLM Integration
**File**: `test_emotions.py` (if exists) or example script
- Shows how to test LLM integration independently

```python
"""
Test script for LLM integration
==============================
This script demonstrates how to test the AI dialogue system
independently from the game.
"""

from ai_dialogue_manager import AIDialogueManager

def test_ai_dialogue():
    """Test the AI dialogue manager with various prompts."""
    ai_manager = AIDialogueManager()
    
    test_prompts = [
        "Hello! How are you today?",
        "I need help with my farm.",
        "What's your favorite crop to grow?",
        "Tell me a joke about farming."
    ]
    
    emotions = ["happy", "sad", "angry", "neutral"]
    
    print("Testing AI Dialogue Generation:")
    print("=" * 40)
    
    for prompt in test_prompts:
        for emotion in emotions:
            response = ai_manager.generate_dialogue_with_context(prompt, emotion)
            print(f"Prompt: {prompt}")
            print(f"Emotion: {emotion}")
            print(f"Response: {response}")
            print("-" * 40)

if __name__ == "__main__":
    test_ai_dialogue()
```

## Key Learning Points
1. Understanding how LLMs work and what they can do
2. How to interact with AI APIs using Python libraries
3. Prompt engineering for better AI responses
4. Handling API responses and errors gracefully
5. Combining multiple AI technologies (emotion detection + LLMs)
6. Creating fallback mechanisms for when AI services are unavailable

## Extension Activities
1. Experiment with different LLM providers (Hugging Face, etc.)
2. Create a dialogue system that remembers conversation history
3. Add personality traits to the AI NPC (grumpy, cheerful, mysterious, etc.)
4. Implement rate limiting to prevent API overuse
5. Create a chatbot interface for testing LLM interactions

## Troubleshooting Tips
- If API calls fail, check your internet connection and API key validity
- Verify that the OpenAI library is properly installed and up to date
- Check for rate limiting or quota exceeded errors from the API provider
- Ensure that your prompts aren't too long (exceeding token limits)
- Look for JSON parsing errors when processing API responses