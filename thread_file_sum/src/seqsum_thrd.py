from threading import Thread, Lock


# thread para somar uma sequencia numérica de um ponto a outro
# e armazenar o resultado em sequence_sum
class SeqSummationThread(Thread):
	
	# atributos compartilhados pelos threads
	sequence_sum = 0

	def __init__(self, num_sequence: list, start: int, end: int, mutex: 'Lock'):
		self.__num_sequence = num_sequence
		self.__start = start
		self.__end = end
		self.__mutex = mutex
		super().__init__()

	def run(self):
		final_sum = self.__seq_summation()

		with self.__mutex:
			self.__class__.sequence_sum += final_sum


	def __seq_summation(self) -> int:
		final_sum = 0

		for i in range(self.__start, self.__end):
			n = int(self.__num_sequence[i])
			final_sum += n

		return final_sum


# função para criar threads SeqSummationThread
def create_seqsum_threads(num_sequence: list, qtd_threads: int = 1):
	threads = []
	mutex = Lock()
	num_sequence_len = len(num_sequence)
		
	# dividindo sequencia em partes iguais por thread
	start = 0
	for i in range(qtd_threads, 0, -1):	
		end = num_sequence_len // i
			
		seqsum_thread = SeqSummationThread(num_sequence, start, end, mutex)
		seqsum_thread.start()
		threads.append(seqsum_thread)
			
		start = end

	for t in threads:
		t.join()

# função para executar soma de uma sequencia
def exec_seqsum(num_sequence: list, qtd_threads: int = 1) -> int:
	create_seqsum_threads(num_sequence, qtd_threads)
	
	return SeqSummationThread.sequence_sum

