#!/bin/bash
for i in "$*"; do
    echo $i
done
python main.py $0 $1