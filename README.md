# Volume_Control_Project

Hand Gesture Volume Control
This repository contains a Python script HandGestureVolumeControl.py that allows you to control the system's master volume using hand gestures detected by the webcam. Below is an overview of the script along with instructions on how to run it.

Script Overview
The HandGestureVolumeControl.py script utilizes the OpenCV library for capturing video frames from the webcam, and it employs the Hand Tracking Module (HandTrackingModule.py) to detect hand landmarks and gestures. The script calculates the distance between the index and thumb fingers to determine the volume level, which is then mapped to control the system's master volume.

Usage
Upon execution, the script will open a window displaying the video feed from the webcam. It will detect your hand and draw landmarks and connections between them. As you perform specific hand gestures (e.g., closing the thumb and index finger), the script will adjust the system's master volume accordingly.

Dependencies
The script requires the following Python libraries:

cv2 (OpenCV)
numpy
comtypes
pycaw

Notes
Make sure you have a working webcam connected to your system.
Adjust the wCam (width) and hCam (height) variables in the script to match your webcam's resolution if needed.
Ensure that your hand is well-illuminated and clearly visible to the webcam for accurate detection.
The script may need to be run with elevated privileges to control the system's master volume.
That's it! You should now be able to control the system's volume using hand gestures detected by the HandGestureVolumeControl.py script.
