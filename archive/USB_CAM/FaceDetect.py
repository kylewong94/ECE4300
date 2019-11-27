import cv2
import sys
import numpy as np 
import time

sys.path.insert(1, '../Utilities/Multithreading')
from threads import *

#####################################################
## Initalizations
#####################################################
MaxFrames = 120
totaltime = []
fpsCap = []

#File Location 
cascPath = "haarcascades/haarcascade_frontalface_default.xml"


#Object Initalize
faceCascade = cv2.CascadeClassifier(cascPath)
#USBCamDev2  = cv2.VideoCapture(0)

#ret, Frame = USBCamDev2.read()

#USBCamDev2.release() 

USBCamDev   = cv2.VideoCapture(0)
#fps = USBCamDev.get(cv2.CAP_PROP_FPS)


#Camera Settings
def make_480p():
	USBCamDev.set(3, 640)
	USBCamDev.set(4, 480)

#def change_res(width, height):
#	USBCamDev.set(3, width)
#	USBCamDev.set(4, height)

#Make Settings
#make_480p()
#change_res(1280, 720)
time1 = time.time()
time2 = time.time()
while (True):
	time1 = time.time()
	ret, Frame = USBCamDev.read()
	Color = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
	faces, Confidence = faceCascade.detectMultiScale2(
		Color,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30,30)
		)
	for (x,y,w,h) in faces:
		cv2.rectangle(Color, (x,y), (x+w, y+h), (0,255,0), 2)

	cv2.imshow('Feed', Color)
	time2 = time.time()
	if cv2.waitKey(1) & 0XFF == ord('q'):
		USBCamDev.release()
		cv2.destroyAllWindows()
		break
	print(str(time2-time1))
