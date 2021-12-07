#!/bin/python3

# TODO
#	remodular a forma de leitura do arquivo, 
#	pois o seek() não está funcionando como esperado


import sys
from threading import Thread, Lock


sequence_sum = 0


class SeqSummationThread(Thread):
	
	def __init__(self, num_sequence: list, start: int, end: int, mutex: 'Lock'):
		self.__num_sequence = num_sequence
		self.__start = start
		self.__end = end
		self.__mutex = mutex
		super().__init__()

	def run(self):
		global sequence_sum
		final_sum = self.__seq_summation()

		with self.__mutex:
			sequence_sum += final_sum


	def __seq_summation(self) -> int:
		final_sum = 0

		for i in range(self.__start, self.__end):
			n = int(self.__num_sequence[i])
			final_sum += n

		return final_sum


def get_file_qtd_lines(file_name):
	fqtd_lines = 0
	with open(file_name, 'r') as f:
		for i in f:
			fqtd_lines += 1

	return fqtd_lines


def create_sequence_sum_threads(file_name, file_qtd_lines, qtd_threads):
	threads = []
	mutex = Lock()
	
	with open(file_name, 'r') as f:
		lines = f.read().splitlines()
	
	frst_line = 0
	for i in range(qtd_threads, 0, -1):	
		lst_line = file_qtd_lines // i
			
		sequence_sum_thread = SeqSummationThread(lines, frst_line, lst_line, mutex)
		sequence_sum_thread.start()
		threads.append(sequence_sum_thread)
			
		frst_line = lst_line

	for t in threads:
		t.join()


def execute_sequence_sum(file_name, file_qtd_lines, qtd_threads):
	global sequence_sum
	create_sequence_sum_threads(file_name, file_qtd_lines, qtd_threads)
		
	return sequence_sum
	

FILE_NAME = sys.argv[1]
FILE_QTD_LINES = get_file_qtd_lines(FILE_NAME)
QTD_THREADS = int(sys.argv[2])

final_sum = execute_sequence_sum(FILE_NAME, FILE_QTD_LINES, QTD_THREADS)

print(final_sum)

