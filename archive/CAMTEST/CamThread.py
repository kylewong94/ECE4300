import threading
from RingBuffer import *
import time 

class CamThread():
    def __init__(self, Cam, ClkCycle):
        self.Cam = Cam
        self.ReturnVal, self.Frame = self.Cam.read()
        self.FrameNo = 0
        self.ClkCycle = ClkCycle

    def CaptureFrames(self, NumOfFrames, Buffer, Sem):
        while(self.FrameNo < NumOfFrames):
            while not Sem.acquire(blocking=False):
                continue
                #print("CamThread: Semaphore is blocked")
            else:
                print("CamThread: Semaphore acquired")
                self.ReturnVal, self.Frame = self.Cam.read()
                print("Putting Image")
                Buffer.Put(self.Frame)
                print("Capturing Frame Number: " + str((self.FrameNo + 1)))
                self.FrameNo+=1
                print("CamThread: Semaphore released")
                Sem.release()
                time.sleep(self.ClkCycle)

    def RunThread(self, NumOfFrames ,object, Sem):
        print("Starting Cam Thread")
        self.Thread = threading.Thread(target = self.CaptureFrames, args = [NumOfFrames, object, Sem])
        self.Thread.start()
