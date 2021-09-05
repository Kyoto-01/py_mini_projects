from estrutura_linear import *


class ListaDuplamenteEncadeada(Lista):

	def __init__(self):
		super().__init__()

	def apontar_para_no(self, no: 'NoDuplo'):
		if self.is_empty():
			self.cabeca = self.cauda = no
		else:
			no.anterior = self.cauda
			no.anterior.proximo = no
			self.cauda = no

	def inserir_no_inicio(self, valor: object):
		novo_elemento = NoDuplo(valor)

		if self.is_empty():
			self.cabeca = self.cauda = novo_elemento
		else:
			novo_elemento.proximo = self.cabeca
			novo_elemento.proximo.anterior = novo_elemento
			self.cabeca = novo_elemento

	def inserir_no_final(self, valor: object):
		novo_elemento = NoDuplo(valor)
		self.apontar_para_no(novo_elemento)

	def remover_do_inicio(self):
		self.assert_not_empty()

		if self.cabeca is self.cauda:
			self.cabeca = self.cauda = None
		else:
			self.remover_elemento(self.cabeca)
			self.cabeca = self.cabeca.proximo

	def remover_do_final(self):
		self.assert_not_empty()

		if self.cabeca is self.cauda:
			self.cabeca = self.cauda = None
		else:
			self.remover_elemento(self.cauda)
			self.cauda = self.cauda.anterior

	def remover_elemento(self, elemento: 'NoDuplo') -> 'NoDuplo':
		if elemento.anterior is not None:
			elemento.anterior.proximo = elemento.proximo
		if elemento.proximo is not None:
			elemento.proximo.anterior = elemento.anterior
		return elemento.anterior

	def remover_ocorrencias(self, valor: object):
		for elem in self:
			if (elem is valor) or (elem.carga == valor):
				self.remover_elemento(elem)


if __name__ == '__main__':

	def teste_remover_ocorrencias():
		vogais = ListaDuplamenteEncadeada()
		vogais.inserir_no_final('a')
		vogais.inserir_no_final('c')
		vogais.inserir_no_final('e')
		vogais.inserir_no_final('i')
		vogais.inserir_no_final('o')
		vogais.inserir_no_final('c')
		vogais.inserir_no_final('c')
		vogais.inserir_no_final('c')
		vogais.inserir_no_final('c')
		vogais.inserir_no_final('u')

		print(vogais)
		vogais.remover_ocorrencias('c')
		print(vogais)

	def teste_remover_de_posicao():
		vogais = ListaDuplamenteEncadeada()
		vogais.inserir_no_final('a')
		vogais.inserir_no_final('e')
		vogais.inserir_no_final('i')
		vogais.inserir_no_final('o')
		vogais.inserir_no_final('u')

		print(vogais)
		vogais.remover_de_posicao(3)
		print(vogais)

	teste_remover_ocorrencias()
	print('***********')
	teste_remover_de_posicao()
