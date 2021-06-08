#!/bin/bash

if [ $# -ne 2 ]; then
	echo "Usage: $0 [from_path] [to_path]"
	exit 1
fi

FILE_SIZE=1024
FROM_PATH=$1
TO_PATH=$2

echo byte elapsed_time_ns

for n in {0..23}; do
	fallocate -l $FILE_SIZE $FROM_PATH/tempfile
	start_time=`date +%s%N`
	mv $FROM_PATH/tempfile $TO_PATH
	rm -rf $TO_PATH/tempfile
	end_time=`date +%s%N`
	result=`expr $end_time - $start_time`
	echo "${FILE_SIZE} ${result}"
	FILE_SIZE=`expr $FILE_SIZE \* 2`
done

