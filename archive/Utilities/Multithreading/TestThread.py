from threads import *
import threading
#Try a simple HelloWorld Testing

def HelloWorld():
	print("Hello World!")


Thread1 = Thread(1, HelloWorld, None)
Thread1.start()

print("Exiting main thread")
