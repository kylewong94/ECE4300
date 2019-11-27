class RingBuffer():
	def __init__(self, Size):
		self.Maxsize = Size
		self.Buffer = [None]*Size
		self.HdPtr = 0
		self.LagPtr = 0

	def getPos(self):
		return self.position

	def get(self, pos):
		if(pos == None):
			return self.Buffer[self.position]
		else:
			return self.Buffer[pos]

	def Next(self):
		if(self.position == self.size-1):
			self.position = 0
			return self.position
		self.position += 1
		return self.position

	def set(self, Value):
		self.Buffer[self.position] = Value


R1 = RingBuffer(5,0)

R1.set(5)
R1.Next()
R1.set(1)
R1.Next()
R1.Next()
R1.Next()

print(R1.getPos())
print(R1.get(None))
print(R1.get(R1.position-1))
print(R1.getPos())
