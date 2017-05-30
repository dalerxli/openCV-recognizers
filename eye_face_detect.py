import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('bp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    eye1 = eyes[0]
    eye2 = eyes[1]
    avgx = (eye1[0] + eye2[0])/2
    avgy = (eye1[1] + eye2[1])/2
    avgw = (eye1[2] + eye2[2])/2
    min_x = min(eye1[0], eye2[0])
    max_x = max(eye1[0], eye2[0])
    min_y = min(eye1[0], eye2[0])
    max_y = max(eye1[0], eye2[0])
    cv2.rectangle(roi_color,(min_x,min_y+30),(max_x+avgw, max_y-30),(0,255,0),2)
    #for (ex,ey,ew,eh) in eyes:
    #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
    #cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/3),(0,0,255),1)
    #cv2.circle(roi_color,(avgx,avgy-50),(avgw/3),(0,0,255),1)
    #cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/16),(255,255,255),1)
    cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/8),(255,255,255),1)
    cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/8+2),(255,0,0),1)
    cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/8+4),(255,255,255),1)
    #cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/4),(255,255,255),1)
    #cv2.circle(roi_color,(avgx+avgw,avgy-50),(avgw/2),(255,255,255),1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
