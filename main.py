import threading
import time
import sys

from CameraThread import CameraThread
from FaceDetection import FaceDetection
from IOThread import IOThread

#parser = argparse.ArgumentParser(description="Frames to run for")
#parser.add_argument('frames', metavar='frames', type=int, help='number of frames to run for')

#args = parser.parse_args()


# change this shit
#run 1
#max_frames = 10
#run 2
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

