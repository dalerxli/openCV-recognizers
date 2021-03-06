from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # eye1 = eyes[0]
        # eye2 = eyes[1]
        # avgx = (eye1[0] + eye2[0])/2
        # avgy = (eye1[1] + eye2[1])/2
        # avgw = (eye1[2] + eye2[2])/2
        # min_x = min(eye1[0], eye2[0])
        # max_x = max(eye1[0], eye2[0])
        # min_y = min(eye1[0], eye2[0])
        # max_y = max(eye1[0], eye2[0])
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        # cv2.rectangle(roi_color,(min_x,min_y+30),(max_x+avgw, max_y-30),(0,255,0),2)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break
