#!/bin/bash

for i in 5000 10000 50000 100000; do 
    python test.py $i > results/NN/$i.log
done
