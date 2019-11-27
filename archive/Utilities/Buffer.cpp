#include "Buffer.h"
#include "Python.h"


Buffer::Buffer()
{
	Buffer = new unsigned char [MAX_BSIZE];

}

Buffer::~Buffer()
{
	delete [] Buffer;
}

void Buffer::StoreBuffer(unsigned char * Message)
{
	Buffer = Message;
}

void Buffer:GetBuffer()
{
	printf("Stored Buffer: %s\n", Buffer);
}




