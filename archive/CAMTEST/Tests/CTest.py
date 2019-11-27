from CamThread import *
import numpy as np
import cv2

sem = threading.Semaphore()

USBCam_1 = cv2.VideoCapture(0)
Cam1 = CamThread(USBCam_1, sem)

Cam1.CaptureFrames(5)
