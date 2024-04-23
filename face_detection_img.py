import cv2
import os
import psutil

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(1)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX 
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 5
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, 'Ugly', (x, y), font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

    pid = os.getpid()
    python_process = psutil.Process(pid)
    memoryUse = python_process.memory_info()[0]/2.**30  # memory use in GB...I think
    cpuUse = python_process.cpu_percent()
    print('memory use:', memoryUse)
    print('cpu use:', cpuUse)
# Release the VideoCapture object
cap.release()
