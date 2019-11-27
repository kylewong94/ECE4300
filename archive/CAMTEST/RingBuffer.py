class RingBuffer:
    def __init__(self):
        self.Buffer = []
    def Put(self, object):
        self.Buffer.append(object)
    def Get(self):
        return self.Buffer.pop()
