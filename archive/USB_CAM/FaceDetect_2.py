import cv2
import numpy as np
import time
import sys

sys.path.insert(1, '../Utilities/Multithreading')
from threads import *

sem = threading.Semaphore()
##########################################
## Inits
##########################################
FramesToCapture = 120

cascPath        = "haarcascades/haarcascade_frontalface_default.xml"
faceCascade     = cv2.CascadeClassifier(cascPath)
##########################################

def CamRead():
	global Return
	global Frame
	global USBCamDev
	global Time1
	global Color
	Run = CamRead()
#	print("Running Cam Read")
	sem.acquire()
	Time1 = time.time()
#	print("CamRead acquired semaphore")
	Return, Frame = USBCamDev.read()
#	print("CamRead released Semaphore")
	Color = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
	faces, Confidence = faceCascade.detectMultiScale2(
		Color,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize=(30,30)
		)
	for (x,y,w,h) in faces:
		cv2.rectangle(Color, (x,y), (x+w, y+h), (0,255,0), 2)
	sem.release()
	time.sleep(0.0002)
	return Run

def RunUSBCam():

	Rerun = RunUSBCam()	
	while not sem.acquire(blocking=False):
#		print("Semaphore not avaiable in RUNUSBCAM")
		time.sleep(0.0001)
	else:
		Rerun = CamRead	
		global Time2
		global Time1
		Time2 = time.time()
		global Color
#		print("Semaphore Received: RUNUSBCAM")
#		print("Running USB CAM")
		cv2.imshow('Feed', Color)
		if cv2.waitKey(1) & 0XFF == ord('q'):
			USBCamDev.release()
			cv2.destroyAllWindows()
		print(str(Time2 - Time1))
		sem.release()
#		print("Sem Released")
		time.sleep(0.0001)
		return ReRun


############################################################
## MAIN PROGRAM
############################################################
CamValInit = cv2.VideoCapture(0)
Return, Frame = CamValInit.read()
CamValInit.release()
Time1 = time.time()
Time2 = time.time()
USBCamDev = cv2.VideoCapture(0)
Color = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
def main():
	ReadThread = threading.Thread(target=CamRead)
	StreamThread = threading.Thread(target=RunUSBCam)
#	FDThread = threading.Thread(target=FaceDetect)
	ReadThread.start()
#	FDThread.start()
	StreamThread.start()

if __name__ == '__main__':
	main()










