from Threading import *

sem = threading.Semaphore()



def HelloWorldTEST():
    print("Hello World from Thread!")



Test = Thread(HelloWorldTEST, sem)
Test2 = Thread(HelloWorldTEST, sem)
Test3 = Thread(HelloWorldTEST, sem)
Test.Run()
Test2.Run()
Test3.Run()
