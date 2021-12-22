#!/bin/python3

# script para somar numeros de um arquivo texto
# utilizando uma quantidade determinada de threads

import sys

from seqsum_thrd import exec_seqsum


def get_file_lines(file_name) -> 'list':	
	with open(file_name, 'r') as f:
		lines = f.read().splitlines()
	
	return lines


FILE_NAME = sys.argv[1]
QTD_THREADS = int(sys.argv[2])

FILE_LINES = get_file_lines(FILE_NAME)
FINAL_SUM = exec_seqsum(FILE_LINES, QTD_THREADS)

print(f'Sum of lines in {FILE_NAME} --> {FINAL_SUM}')

