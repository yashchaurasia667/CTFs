#!/bin/bash

sub='pico'

base64 -d enc_flag > ans
decoded=$(cat ans)

echo "decoded= $decoded"
echo -n "answer= "
cat ans

while [ "$decoded"!="$sub"* ];
do
	cat ans | base64 -d > ans
	cat ans
	decoded=$(cat ans)
done

echo broken
cat ans