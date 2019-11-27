from FileIOThread import *



USBCam_1 = cv2.VideoCapture(0)
IOFile   = IOFile()

ret, frame = USBCam_1.read()

IOFile.WriteImage(1, frame)
