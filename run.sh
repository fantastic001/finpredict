#!/bin/bash

for i in 5000 10000 50000 100000; do 
    python test.py $i > results/AR-20d-log/$i.log
done
