from picamera.array import PiRGBArray
from picamera import PiCamera
import time, datetime
import cv2

ball_cascade = cv2.CascadeClassifier('ball.xml')

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 120
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(0.1)

counter = FramesCounter().start()

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    counter.update()
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    balls = ball_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2, minSize=(10,10))
    for (x,y,w,h) in balls:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        counter.stop()
        break

class FramesCounter:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()

    def stop(self):
        self._end = datetime.datetime.now()
        print numFrames/((end-start).total_seconds())

    def update(self):
        self._numFrames+=1
