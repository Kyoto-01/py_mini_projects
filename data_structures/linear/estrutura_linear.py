from abc import ABC, abstractmethod


class No:

	def __init__(self, carga: object = None, proximo: 'No' = None):
		self.carga = carga
		self.proximo = proximo

	def __str__(self):
		return str(self.carga)


class NoDuplo(No):

	def __init__(self, carga: object = None, proximo: 'NoDuplo' = None, anterior: 'NoDuplo' = None):
		super().__init__(carga, proximo)
		self.anterior = anterior


class EstruturaLinear:

	def __init__(self):
		self.cabeca: 'No' = None

	def __iter__(self):
		atual = self.cabeca
		while atual is not None:
			yield atual
			atual = atual.proximo

	def __len__(self):
		contador = 0
		for elem in self:
			contador += 1
		return contador

	def __str__(self):
		str_retorno = ''
		for elem in self:
			str_retorno += f'{elem} '
		return f'[{str_retorno}]'

	def index_of(self, elemento):
		contador = 0
		for elem in self:
			if (elem is elemento) or (elem.carga == elemento):
				return contador
			contador += 1
		return -1

	def is_empty(self):
		return self.cabeca is None

	def assert_not_empty(self):
		assert not self.is_empty(), f'A {self.__class__.__name__} está vazia!'


class Lista(EstruturaLinear, ABC):

	def __init__(self):
		super().__init__()
		self.cauda = None

	@abstractmethod
	def apontar_para_no(self, no: 'No'):
		pass

	@abstractmethod
	def inserir_no_inicio(self, valor: object):
		pass

	@abstractmethod
	def inserir_no_final(self, valor: object):
		pass

	@abstractmethod
	def remover_do_inicio(self):
		pass

	@abstractmethod
	def remover_do_final(self):
		pass

	@abstractmethod
	def remover_elemento(self, elemento: 'No') -> 'No':
		pass

	def remover_de_posicao(self, posicao: int):
		assert 0 <= posicao < len(self), f'A posição {posicao} é inválida, {self.__class__.__name__} possui apenas {len(self)} elemento(s)'

		if posicao == 0:
			self.remover_do_inicio()
		elif posicao == (len(self) - 1):
			self.remover_do_final()
		else:
			contador: int = 0
			for elem in self:
				if contador == posicao:
					self.remover_elemento(elem)
					break
				contador += 1
