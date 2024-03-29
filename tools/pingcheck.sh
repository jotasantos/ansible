#!/bin/bash
date
cat ./pingchecklist-$1.txt |  while read output
do
    ping -c 1 "$output" > /dev/null
    # $? in bash is the status of the last executed program
    if [ $? -eq 0 ]; then
    echo "node $output is up" 
    else
    echo "node $output is down"
    fi
done
