from RingBuffer import *
import cv2
import threading
import time
class IOFileThread():
    def __init__(self, ClkCycle):
        self.WritePath     = "WriteFrameTest_20/"
        self.FileName      = ""
        self.MaxFrames     = 0
        self.FramesWritten = 0
        self.ClkCycle      = ClkCycle

    def WriteImage(self, Frames, Buffer, Sem):
        self.MaxFrames = Frames
        while (self.FramesWritten < self.MaxFrames):
            while not Sem.acquire(blocking=False):
                continue
#                print("IOThread: Semaphore is blocked")
            else:
                print("FileIO: acquired Semaphore")
                self.FileName = ("Image_" + str(self.FramesWritten + 1) + ".jpg")
                try:
                    print("Writing " + self.FileName)
                    Frame = Buffer.Get()
                    Color = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('Frame', Color)
                    cv2.imwrite((self.WritePath+self.FileName), Frame)
                except:
                    print("Buffer Empty")
                self.FramesWritten += 1
                print("FileIO: released Semaphore")
                Sem.release()
                time.sleep(self.ClkCycle)

    def RunThread(self, Frames, object, Sem):
        print("File I/O thread starting . . .")
        self.Thread = threading.Thread(target = self.WriteImage, args = [Frames, object, Sem])
        self.Thread.start()


