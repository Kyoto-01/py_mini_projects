#!/bin/bash

# script para testar os tempos de execução (real, kernel e user)
# e a quantidade de memória gastos pelo script "file_summation.py"
# lendo o arquivo "tests/nums.txt" de acordo com a quantidade de threads usados

REPEAT=$1

QTDS_THREADS=(1 2 3 4 10)


# criando/atualizando arquivos para salvar resultados
> times.txt
> mem.txt

for t in ${!QTDS_THREADS[*]}
do
	# número do caso atual
	CASE=$(( ${t} + 1 ))

	# variáveis de utilização de recursos do caso t
	real_times=0
	kernel_times=0
	usr_times=0
	mem_usage=0

	# interface com o usuário
	echo "teste caso ${CASE}"

	# coletando dados de utilização de recursos do caso t
	for r in $( seq 1 ${REPEAT} )
	do
		/usr/bin/time --format="%E|%S|%U|%M" ./file_summation.py tests/nums.txt ${QTDS_THREADS[${t}]} > /dev/null 2> infos.txt
		
		real_times=$( bc <<< "scale=2;${real_times} + $( cat infos.txt | cut -d '|' -f 1 | cut -d ':' -f 2 )" )
		kernel_times=$( bc <<< "scale=2;${kernel_times} + $( cut -d '|' -f 2 < infos.txt )" )
		usr_times=$( bc <<< "scale=2;${usr_times} + $( cut -d '|' -f 3 < infos.txt )" )
		mem_usage=$( bc <<< "scale=2;${mem_usage} + $( cut -d '|' -f 4 < infos.txt )" )
	done		

	# calculando médias
	real_times=$( bc <<< "scale=2;${real_times} / ${REPEAT}" ) 
	kernel_times=$( bc <<< "scale=2;${kernel_times} / ${REPEAT}" ) 
	usr_times=$( bc <<< "scale=2;${usr_times} / ${REPEAT}" ) 
	mem_usage=$( bc <<< "scale=2;${mem_usage} / ${REPEAT}" ) 
	
	echo -e "caso ${CASE}\t${real_times}\t0.1\t${kernel_times}\t0.2\t${usr_times}\t0.3" >> times.txt
	echo -e "caso ${CASE}\t${mem_usage}\t1" >> mem.txt

done

# gerando gráficos
gnuplot -p < charttime.gpi
gnuplot -p < chartmem.gpi

# excluindo arquivos de apoio criados pelo script
rm -f infos.txt

