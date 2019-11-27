from CamThread import *
from FileIOThread import *
from RingBuffer import *

#########################################
## Initializations
#########################################
USBCam     = cv2.VideoCapture(0)
Mutex      = threading.Semaphore()

CamCycle   = 0.01
FileCycle  = 0.02
MaxFrames  = 20

ImgBuffer  = RingBuffer()
CamThread  = CamThread(USBCam, CamCycle)
FileThread = IOFileThread(FileCycle)

#########################################

#########################################
## Main Program
#########################################
def main():
    CamThread.RunThread(MaxFrames, ImgBuffer, Mutex)
    FileThread.RunThread(MaxFrames, ImgBuffer, Mutex)


if __name__ == '__main__':
    main()
    print("Main Finished")

#########################################

#print("Main Finished")
