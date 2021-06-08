#!/bin/bash

if [ $# -ne 4 ]; then
	echo "Usage: ./run.sh [upper_layer] [lower_layer] [merged_layer] [policy]"
	exit 1
fi

cd ..
python3 harmonyfs_main.py $1 $2 $3 $4
