import threading
import numpy as np
import cv2

class FaceDetection(threading.Thread):

    def __init__(self, max_frames, lock1, lock2, shared1, shared2):
        threading.Thread.__init__(self)
        self.frame_count = 0
        self.max_frames = max_frames

        self.lock1 = lock1
        self.lock2 = lock2
        self.shared1 = shared1
        self.shared2 = shared2
        self.buffer1 = []
        self.buffer2 = []

    def run(self):

        casc_path = "haarcascades/haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(casc_path)
        
        while(self.frame_count != self.max_frames):

            if(len(self.buffer1) > 0):
                frame = self.buffer1.pop(0)
                color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                faces, confidence = face_cascade.detectMultiScale2(
                    frame,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30,30)
                    )

                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                
                self.buffer2.append(frame)

            if(self.lock1.locked() is False):
                self.lock1.acquire()
                #print("FaceThread: Putting frame in self buffer" + str(self.frame_count))
                self.buffer1.extend(self.shared1)
                self.shared1.clear()
                self.lock1.release()

            if(len(self.buffer2) > 0 and self.lock2.locked() is False):
                self.lock2.acquire()
                self.frame_count += len(self.buffer2)
                print("FaceThread: Putting Frame " + str(self.frame_count) + " in Buffer2")
                self.shared2.extend(self.buffer2)
                self.buffer2.clear()
                self.lock2.release()

