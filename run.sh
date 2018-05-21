#!/bin/bash

echo "The number of parameters is: $#"
for i in "$*"; do
    echo $i
done
echo "The input file is: $0"
echo "The output file is: $1"
python main.py $0 $1