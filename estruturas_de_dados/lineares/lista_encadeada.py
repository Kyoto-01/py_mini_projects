from estrutura_linear import *


class ListaEncadeada(Lista):

	def __init__(self):
		super().__init__()

	def apontar_para_no(self, no: 'No'):
		if self.is_empty():
			self.cabeca = self.cauda = no
		else:
			self.cauda.proximo = no
			self.cauda = no

	def inserir_no_inicio(self, valor: object):
		novo_elemento = No(valor)

		if self.is_empty():
			self.cabeca = self.cauda = novo_elemento
		else:
			novo_elemento.proximo = self.cabeca
			self.cabeca = novo_elemento

	def inserir_no_final(self, valor: object):
		novo_elemento = No(valor)
		self.apontar_para_no(novo_elemento)

	def remover_do_inicio(self):
		self.assert_not_empty()

		if self.cabeca is self.cauda:
			self.cabeca = self.cauda = None
		else:
			self.cabeca = self.cabeca.proximo

	def remover_do_final(self):
		self.assert_not_empty()

		if self.cabeca is self.cauda:
			self.cabeca = self.cauda = None
		else:
			self.cauda = self.remover_elemento(self.cauda)

	def remover_elemento(self, elemento: 'No') -> 'No':
		atual: 'No' = self.cabeca
		while atual.proximo is not elemento:
			atual = atual.proximo
		atual.proximo = atual.proximo.proximo

		return atual

	def concatenar_estruturas(self, *estruturas: 'ListaEncadeada'):
		for est in estruturas:
			if self.is_empty():
				self.cabeca = est.cabeca
			else:
				self.cauda.proximo = est.cabeca
			self.cauda = est.cauda


if __name__ == '__main__':

	def concatenacao_listas():
		lista1: 'ListaEncadeada' = ListaEncadeada()
		lista1.inserir_no_final(1)
		lista1.inserir_no_final(7)
		print(f'prim: {lista1}')

		lista2: 'ListaEncadeada' = ListaEncadeada()
		lista2.inserir_no_final(3)
		lista2.inserir_no_final(4)
		lista2.inserir_no_final(8)
		print(f'sec: {lista2}')

		lista3: 'ListaEncadeada' = ListaEncadeada()
		lista3.concatenar_estruturas(lista1, lista2)
		print(f'terc: {lista3}')


	def segmentar_pares_de_impares(numeros: 'ListaEncadeada') -> ('ListaEncadeada', 'ListaEncadeada'):
		pares = ListaEncadeada()
		impares = ListaEncadeada()

		for no in numeros:
			if no.carga % 2 == 0:
				pares.apontar_para_no(no)
			else:
				impares.apontar_para_no(no)
		pares.cauda.proximo = impares.cauda.proximo = None

		return pares, impares


	def teste_segmentar_pares_de_impares():
		nums = ListaEncadeada()
		nums.inserir_no_final(1)
		nums.inserir_no_final(2)
		nums.inserir_no_final(6)
		nums.inserir_no_final(7)
		nums.inserir_no_final(8)
		print(f'início: {nums}')

		par, impar = segmentar_pares_de_impares(nums)

		print(f'par: {par}')
		print(f'ímpar: {impar}')

	def remocao():
		nums = ListaEncadeada()
		nums.inserir_no_final(1)
		nums.inserir_no_final(2)
		nums.inserir_no_final(6)
		nums.inserir_no_final(7)
		nums.inserir_no_final(8)
		print(f'início: {nums}')  # 1 2 6 7 8

		nums.remover_do_inicio()
		nums.remover_do_final()
		print(f'início: {nums}')  # 2 6 7

		nums.remover_de_posicao(1)
		print(f'início: {nums}')  # 2 7

	concatenacao_listas()
	print('**************')
	teste_segmentar_pares_de_impares()
	print('**********')
	remocao()
