#!/bin/bash

# script para gerar uma determinada quantidade de
# números(qtd) em um determinado range(max)

qtd=$1	# number of lines
max=$2	# max number to generate

if [ -z ${qtd} -o -z ${max} ]
then
	echo "preencha os parâmetros corretamente"
	echo "usage: $0 <number> <number>"
	exit 1
fi

for i in $( seq 1 ${qtd} )
do
	echo $(( ${RANDOM} % ${max} ))	
done
