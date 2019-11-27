from threads import *

def Writer(Args):
	Args[0]  = "Changed by Writer"
	Args[1]  = "Changed by Writer"

def Reader_1(Args):
	print(Args[0] + " Read by Reader_1")

def Reader_2(Args):
	print(Args[1] + "Read by Reader_2")

Values = []
Values = ["Unchanged by Anything", "Unchanged by Anything"]

print("Before Thread Execution")
print(Values[0])
print(Values[1])

Thread1 = Thread(1, Writer, Values)
Thread2 = Thread(2, Reader_1, Values)
Thread3 = Thread(3, Reader_2, Values)

Thread1.start()
Thread2.start()
Thread3.start()

#Thread1.join()
#Thread2.join()
#Thread3.join()
print("Exiting Main Thread")

print("After Thread Execution")
print(Values[0])
print(Values[1])


