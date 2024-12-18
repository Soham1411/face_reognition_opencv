# Face Recognition and Detection Project using OpenCV

This project demonstrates two functionalities:

1. **Real-Time Face Detection**: Utilizes OpenCV's Haar Cascade Classifier to detect faces in real-time from a webcam feed.
2. **Face Recognition**: Recognizes faces using a pre-trained Local Binary Patterns Histogram (LBPH) model, trained on a given dataset of faces.

---

## Features

### Face Detection
- Detects faces in real-time using a webcam.
- Uses OpenCV's Haar Cascade Classifier for face detection.
- Draws rectangles around detected faces.

### Face Recognition
- Identifies faces from the given dataset.
- Trained using OpenCV's LBPH face recognizer.
- Outputs the recognized person's name and confidence score.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Soham1411/face_reognition_opencv.git
   ```

2. Navigate to the project directory:
   ```bash
   cd face_recognition_codes
   cd face_detection_codes
   ```

3. Install required dependencies:
   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```

---

## Usage

### Real-Time Face Detection

1. Ensure the `haar_face.xml` file is in the project directory.
2. Run the detection script:
   ```bash
   python face_detect1.py
   ```
3. Press `q` to exit the real-time detection window.

### Face Recognition

1. Place the training dataset in the `faces/` directory.
2. Train the recognizer (script provided):
   ```bash
   python face_train.py
   ```
3. Run the recognition script:
   ```bash
   python face_recognition.py
   ```

---

## File Structure

```
face_recognition_codes and face_detection_codes/
│
├── haar_face.xml                 # Haar Cascade Classifier file
├── face_detect1.py               # Real-time face detection script
├── face_recognition.py           # Face recognition script
├── face_train.py                 # Training script for the LBPH recognizer
├── features.npy                  # Extracted features (generated during training)
├── labels.npy                    # Corresponding labels (generated during training)
├── face_trained.yml              # Trained LBPH model
├── faces/                        # Directory containing training images
├── README.md                     # Project documentation
```

---

## Resources and Credits

- **OpenCV**: [GitHub Repository](https://github.com/opencv/opencv)
- **Haar Cascade Classifier Files**: [Download Haar Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Any suggestions or improvements are welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
