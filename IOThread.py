import threading
import numpy as np
import cv2

class IOThread(threading.Thread):

    def __init__(self, max_frames, lock, shared):
        threading.Thread.__init__(self)
        self.frame_count = 0
        self.lock = lock
        self.max_frames = max_frames
        self.shared = shared
        self.buffer = []

    def run(self):
        write_path = "images/frame-{}.jpg"

        while(self.frame_count != self.max_frames):
            if(len(self.buffer) > 0): 
                color = self.buffer.pop(0)
                self.frame_count += 1
                print("IOTHREAD: Writing FrameNo: " + str(self.frame_count))
                cv2.imwrite(write_path.format(self.frame_count), color)

            if(self.lock.locked() is False):
                self.lock.acquire()
                self.buffer.extend(self.shared)
                self.shared.clear()
                self.lock.release()

            #print("IO THREAD RUNNING")	
