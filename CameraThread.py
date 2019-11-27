import threading
import numpy as np
import cv2

class CameraThread(threading.Thread):

    def __init__(self, max_frames, lock, shared):
        threading.Thread.__init__(self)
        self.frame_count = 0
        self.max_frames = max_frames

        self.lock = lock
        self.shared = shared
        self.buffer = []

        self.iter = 0

    def run(self):
        USBCamDev = cv2.VideoCapture(0)
        while(self.frame_count != self.max_frames):
            
            ret, frame = USBCamDev.read()
            self.buffer.append(frame)            
            
            if(len(self.buffer) > 0 and self.lock.locked() is False):
                self.lock.acquire()
                self.frame_count += len(self.buffer)
                print("CameraThread: Grabbing Frame" + str(self.frame_count))
                self.shared.extend(self.buffer)
                self.buffer.clear()
                self.lock.release()

