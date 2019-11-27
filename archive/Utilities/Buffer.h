/////////////////////////////////////////////////////////////
// Buffer class to transfer data between Python scripts and C
/////////////////////////////////////////////////////////////
#ifndef BUFFER__H
#define BUFFER__H

class Buffer
{
	private:
		unsigned int MAX_BSIZE = 128;

		unsigned char * Buffer;

	public:
		Buffer();
		~Buffer();
	
		void StoreBuffer(unsigned char * Message);
		void GetBuffer();
		void ClearBuffer(); 
}

#endif
