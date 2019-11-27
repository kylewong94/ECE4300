import numpy as np
import cv2 


#Give cv a object to hold
USBCamDev = cv2.VideoCapture(0)

#Error checking
if not (USBCamDev.isOpened()):
	print("USB Camera can not be opened")

#Start Live Video Stream
while(True):
	ret, Feed = USBCamDev.read()

	Color = cv2.cvtColor(Feed, cv2.COLOR_BGR2HSV)

	cv2.imshow('Feed', Feed)

#Set up Break Key
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

USBCamDev.release()
cv2.destroyAllWindows()


