# Day 2: Facial Recognition Model Training

## Objective
Learn model training concepts and implement expression recognition.

## Core Concepts
- **Model Training Fundamentals**
  - Training vs. validation vs. test data
  - Small dataset of facial expressions (happy, sad, neutral)
  - Students capture labeled images
- **Implementing Training Pipeline**
  - Code walkthrough for training/fine-tuning expression models
  - Focus on understanding how models learn from data
- **Testing & Evaluating Models**
  - Run model on test images
  - Print accuracy and confusion matrix
- **Saving Models**
  - Save trained model to file (`.h5` or `.pkl`)
  - Loading models for game integration

## Hands-On Exercise
- Follow guided notebook/script to train expression recognition model
- Test on personal images or sample photos
- Check and discuss accuracy results

## Code References

### Jupyter Notebooks for Training
**File**: `ai_materials/02_real_time_emotion_detection.ipynb`
- Shows the complete workflow for emotion detection training
- Demonstrates data collection, preprocessing, and model training

### Emotion Detector Implementation Details
**File**: `emotion_detector.py` (Lines 50-150)
- Shows how the emotion detection model is used for predictions
- Demonstrates image preprocessing and emotion classification

```python
    def detect_emotion(self, frame):
        """Detect emotion from a video frame."""
        if not self.model_loaded or self.emotion_model is None:
            return "unknown", 0.0
            
        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        if len(faces) == 0:
            return "no_face", 0.0
            
        # Process the first detected face
        (x, y, w, h) = faces[0]
        face_roi = gray[y:y+h, x:x+w]
        
        # Preprocess for emotion model
        face_roi = cv2.resize(face_roi, (48, 48))
        face_roi = face_roi.astype("float") / 255.0
        face_roi = np.expand_dims(face_roi, axis=-1)
        face_roi = np.expand_dims(face_roi, axis=0)
        
        # Predict emotion
        try:
            preds = self.emotion_model.predict(face_roi)[0]
            emotion_probability = np.max(preds)
            emotion_label = self.emotion_labels[np.argmax(preds)]
            return emotion_label, emotion_probability
        except Exception as e:
            print(f"⚠️ Error in emotion prediction: {e}")
            return "error", 0.0
```

### Model Loading and Usage
**File**: `emotion_detector.py` (Lines 150-200)
- Shows how to start/stop video capture
- Demonstrates real-time emotion detection loop

```python
    def start_detection(self):
        """Start video capture for emotion detection."""
        if self.is_running:
            return
            
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            print("⚠️ Could not open video device")
            return False
            
        self.is_running = True
        return True
    
    def stop_detection(self):
        """Stop video capture and release resources."""
        if self.video_capture is not None:
            self.video_capture.release()
        self.is_running = False
    
    def get_emotion(self):
        """Get current emotion detection result."""
        if not self.is_running or self.video_capture is None:
            return "not_running", 0.0
            
        ret, frame = self.video_capture.read()
        if not ret:
            return "no_frame", 0.0
            
        return self.detect_emotion(frame)
```

### Integration with Game Systems
**File**: `main.py` (Lines 200-250)
- Shows how emotion detection is integrated into the game
- Demonstrates toggling emotion detection and using results

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
            # Could use emotion to influence game state or dialogue
            if emotion != "not_running" and emotion != "no_face":
                # Store current emotion for dialogue system
                self.current_emotion = emotion
                self.current_emotion_confidence = confidence
```

## Key Learning Points
1. Understanding the machine learning workflow (data → training → evaluation → deployment)
2. How convolutional neural networks work for image classification
3. Image preprocessing techniques for model input
4. Real-time video processing with OpenCV
5. Model persistence and loading for reuse
6. Integrating AI models into interactive applications

## Extension Activities
1. Collect your own facial expression dataset and retrain the model
2. Modify the emotion detector to work with static images instead of video
3. Add emotion smoothing to reduce jitter in predictions
4. Create a confidence visualization for emotion detection results
5. Experiment with different model architectures for emotion recognition

## Troubleshooting Tips
- If the model fails to load, check that the file path is correct and the file isn't corrupted
- Verify that TensorFlow/Keras is compatible with your Python version
- Ensure webcam is properly connected and not being used by another application
- Check that the Haar cascade XML file is accessible
- Look for dimension mismatches in image preprocessing steps