#!/bin/bash

# script para obter a soma dos números nas linhas de um arquivo
# para fins de comparação com o script "file_summation.py"

file=$1
fsum=0

for l in $( cat ${file} )
do
	echo $l
	fsum=$(( ${fsum} + $l ))
done

echo ${fsum}
