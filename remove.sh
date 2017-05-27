#!/bin/bash

cat $1 | while read LINE
do
    limit=5
    lines="$(cat out/$LINE | wc -l)"

    if [ "$lines" -gt "$limit" ]; then
        echo "Corrected"
        head -n -26 out/$LINE > corrected/$LINE
    fi
done
