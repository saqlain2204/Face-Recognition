# Real-time Face Recognition :smiley:

This Python script uses the `face_recognition` library and OpenCV to perform real-time face recognition from a webcam. It loads known faces from a specified folder, captures video frames from the webcam, and detects faces in the frames. It then compares the detected faces with the known faces to recognize individuals in real-time. The recognized names are displayed on the video frames.

## Requirements

- Python 3.x
- OpenCV (cv2)
- face_recognition
- NumPy

You can install the required packages using the following commands:

```python 
pip install opencv-python
pip install face-recognition
pip install numpy
```

## Usage

1. Clone the repository to your local machine:
`git clone <repository_url>`


2. Run the `face_recognition.py` script: 
`python face_recognition.py`


3. Enter the folder path containing the known faces when prompted. The script will load the known faces from the specified folder.

4. The script will start capturing video frames from the webcam and performing real-time face recognition.

5. Recognized names will be displayed on the video frames.

6. Press 'q' to quit the script.

Note: The script assumes that there is only one face per image in the known faces folder, and the images are in JPG format. If the script encounters any issues with loading or encoding the images, it will skip those images and continue with the rest.

Feel free to customize the code to suit your specific requirements, such as changing the face recognition parameters, video frame size, or display settings.

### Happy face recognition! :smile:
