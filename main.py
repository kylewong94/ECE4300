import threading
import time
import sys

from CameraThread import CameraThread
from FaceDetection import FaceDetection
from IOThread import IOThread

max_frames = int(sys.argv[1])

# mulithreading stuff
shared1 = []
shared2 = []
lock1 = threading.Lock()
lock2 = threading.Lock()

threads = [CameraThread(max_frames, lock1, shared1), 
            FaceDetection(max_frames, lock1, lock2, shared1, shared2),
            IOThread(max_frames, lock2, shared2)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

