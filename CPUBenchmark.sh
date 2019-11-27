#!/bin/bash
#Script file to run CPU analyzation to output to file

SECONDS=$1
INTERVALS=$2
FRAMES=$3
FACES=$4
FolderName=Test_NOCOLOR_FRAMES_${FRAMES}_FACES_${FACES}

sar $SECONDS $INTERVALS >> CPUBM_S${SECONDS}_I${INTERVALS}_F${FRAMES}.out

echo "CPU analyzing finished, performing last processes . . . ;)"

echo "Creating Test Folder"
cd TestBenchData
mkdir $FolderName

echo "Moving Test Bench Information"
cd ../
mv *.out ./TestBenchData/$FolderName

echo "Moving images"
cd images	
mv *.jpg ../TestBenchData/$FolderName

cd ..

echo "Moving time files"
mv *.time ./TestBenchData/$FolderName

echo "Bench mark completed"
