#!/bin/bash

file=$1
fsum=0

for l in $( cat ${file} )
do
	echo $l
	fsum=$(( ${fsum} + $l ))
done

echo ${fsum}
