#!/bin/bash

echo "Moving Benchmark Data . . ."
mv *.out TestBenchData

echo "Removing Images . . ."
cd images && rm *.jpg
