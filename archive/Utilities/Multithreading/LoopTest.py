from threads import *

def Test():
	print("running first while loop")
	while(1):
		print("J")	
def Test2():
	print("running second while loop")
	while(1):
		print("K")

def main():
	T1 = threading.Thread(target=Test)
	T2 =threading.Thread(target=Test2)
	T1.start()
	T2.start()

if __name__ == '__main__':
	main()
