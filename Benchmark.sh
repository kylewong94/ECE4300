#!/bin/bash

Frames=$1
Seconds=$2
Intervals=$3
Faces=$4

CPU="bash CPUBenchmark.sh $Seconds $Intervals $Frames $Faces"
Time=$(date +"%T")

echo "Starting CPU Benchmarking:"
echo "	Seconds:   $Seconds"
echo "	Intervals: $Intervals"

$CPU &

echo "Beginning Facial Recognization:"
echo "	Frames: $Frames"
echo "	Faces:  $Faces"
echo "Start Time: $Time" >> start.time 
(time python3 main.py ${Frames}) 2>  runtime.time
