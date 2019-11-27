################################################
## ECE4300 Project 
## Threading.py Class
################################################
import threading
import time


class Thread:
    def __init__(self, Function, Sem):
        self.Function = Function
        self.Sem = Sem
        self.Thread = threading.Thread(target = self.Function)    
    def Run(self):
        print("Mutex Acquired")
        self.Sem.acquire()
        try:
            print("Running Thread")
            return self.Thread.start()
        finally:
            print("Releasing Mutex")
            self.Sem.release()
