from RingBuffer import * 
from CamThread import *
import numpy as np
import cv2

USBCam = cv2.VideoCapture(0)
sem = threading.Semaphore()

TestBuffer = RingBuffer()
TestCam = CamThread(USBCam, sem)


def main():
    TestCam.RunThread(1, TestBuffer)

if __name__ == '__main__':
    main()


#cv2.imshow('Feed', TestBuffer.Get())
USBCam.release()
ucv2.destroyAllWindows()

