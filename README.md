
##Purpose##
Facial Recognition with OpenCV and face_recognition
This project implements a simple facial recognition system using OpenCV and the face_recognition library. 
It captures video from a webcam and identifies known faces in real-time, displaying the name of the recognized person on the video feed.
The goal is to recognise and label faces in a live video stream based on aset of pre-loaded images of knwon individuals.

##Requirements##
Before you can run this project, make sure you have the following libraries installed:

Python 3.x
OpenCV (cv2)
face_recognition
##How It Works##
Load Known Faces: The program loads images of known people and encodes their facial features.
Capture Webcam Video: It initializes the webcam and continuously captures video frames.
Face Detection and Recognition: For each frame captured from the webcam, the program detects faces, encodes them, and compares them to the known face encodings.
Display Results: If a match is found, the program draws a rectangle around the face and displays the name of the recognized person. If no match is found, it labels the face as "unknown".
Quit: The video feed can be stopped by pressing the q key.
# Face_Recognition
