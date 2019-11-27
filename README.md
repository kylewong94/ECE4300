# ECE 4300 Project
Benchmarking CPU performance on a Raspberry Pi 3 that is running facial recognition software.
Project is for ECE 4300 - Computer Architecture.

**Members**:
Kyle Wong, George Kotobuki, Edan Nankin, Kenneth Livingword, Athan Alcala

# Hardware
Platform: Raspberry Pi 3
Linux Distro: ArchLinux ARM 

# Current development operating system
Ubuntu 18.04

# Software
Main USB Camera Library:
Facial Recognization Software:	Python3.6.8 | OpenCV 3.2 | Python3-tk 3.6.8

To run:
```python
./Benchmark.sh <frames> <time> <interval> <faces>
```
  **frames** are the number of frames to run for  
  **time** is the time in seconds to run benchmark for  
  **interval** is the time in seconds between each benchmark output  
  **faces** is the number of faces  
